from seleniumbase import BaseCase
from seleniumbase import SB
from flask import Flask, jsonify

app = Flask(__name__)

class Job:
    def __init__(self, type_of_job, company_name, job_title, salary, traffic, working_hours, detailed_url, image_url):
        self.type_of_job = type_of_job
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary
        self.traffic = traffic
        self.working_hours = working_hours
        self.detailed_url = detailed_url
        self.image_url = image_url

def scrape_jobs(url):
    jobs = []
    with SB(undetectable=True, enable_3d_apis=False, headless=True,headless2=True) as sb:
        sb.open(url)
        sb.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Find the element for scrolling
        element_scroll = sb.find_element(".TM-adnetJobCassette__inner")
        sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", element_scroll)
        
        elements = sb.find_elements(".TM-adnetJobCassette.js-recordJobSeenCassette")
        
        for element in elements:
            try:
                type_of_job = element.find_element("css selector", ".TM-adnetJobCassette__tag").text
                company_name = element.find_element("css selector", ".TM-adnetJobCassette__company").text
                job_title = element.find_element("css selector", ".TM-adnetJobCassette__jobTtl").text
                
                miscellaneous = element.find_elements("css selector", ".TM-adnetJobCassette__recruitInfoTbl--txt")
                
                # Check if miscellaneous list has enough elements
                if len(miscellaneous) >= 3:  # Ensure at least 3 elements in the list
                    salary = miscellaneous[0].text
                    traffic = miscellaneous[1].text
                    working_hours = miscellaneous[2].text
                else:
                    salary = "N/A"
                    traffic = "N/A"
                    working_hours = "N/A"
                
                image_url_element = element.find_element("css selector", ".TM-adnetJobCassette__imgDetail--main")
                image_url = image_url_element.get_attribute("src")
                
                detailed_url_element = element.find_element("css selector", ".TM-adnetJobCassette__link")
                detailed_url = detailed_url_element.get_attribute('href')
                
                job = Job(type_of_job, company_name, job_title, salary, traffic, working_hours, detailed_url, image_url)
                jobs.append(job)
                #sb.quit()
            except Exception as e:
                # Handle any exceptions during job data extraction
                #sb.quit()
                print(f"Error extracting job details: {e}")
    
    return jobs