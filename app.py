from flask import Flask, jsonify, request
from flask_caching import Cache
import getJobsNearByApi
from createUrl import GenerateUrl
#import logging
app = Flask(__name__)
cache = Cache(app)
app.config['CACHE_TYPE'] = 'simple'
# Instantiate GenerateUrl class
generator = GenerateUrl()
#logging.basicConfig(level=logging.DEBUG) 
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask-SeleniumBase Integration'})

@app.route('/fetch-jobs', methods=['GET'])
def fetch_jobs_route():
    #logging.debug("Executing example_route") 
    try:
        state_name = request.args.get('state_name')
        nearest_station = request.args.get('nearest_station')
        occupation = request.args.get('occupation')
        employment_status = request.args.get('employment_status')
        free_word = request.args.get('free_word')
        language = request.args.get('language')
        #logging.debug(f"Received request with parameters: state_name={state_name}, nearest_station={nearest_station}, occupation={occupation}, employment_status={employment_status}, free_word={free_word}, language={language}")
       
        # Generate the search URL using the GenerateUrl instance
        url = generator.generate_url(state_name=state_name, nearest_station=nearest_station,
                                     occupation=occupation, employment_status=employment_status,
                                     free_word=free_word, language=language)
        
        # Scrape jobs using the generated URL
       
        jobs_list = getJobsNearByApi.scrape_jobs(url=url)
        # Prepare job data for JSON response
        jobs_data = [{'type_of_job': job.type_of_job,
                      'company_name': job.company_name,
                      'job_title': job.job_title,
                      'salary': job.salary,
                      'traffic': job.traffic,
                      'working_hours': job.working_hours,
                      'detailed_url': job.detailed_url,
                      'image_url': job.image_url} for job in jobs_list]

        # Return job data as JSON response
        return jsonify({'status': 'success', 'total-matches':len(jobs_data),'url':url,'jobs': jobs_data})
        

    except Exception as e:
        # Handle any exceptions that may occur during job fetching
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/cached-route')
@cache.cached(timeout=60)  # Cache this route for 60 seconds
def cached_route():
    return jsonify({'status': 'success', 'message': 'Cached response'})

if __name__ == '__main__':
    app.run(debug=True)
