from selenium import webdriver
from seleniumbase import BaseCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BaseCase.main(__name__, __file__)





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

class OverrideDriverTest(BaseCase):
    def get_new_driver(self, *args, **kwargs):
        """This method overrides get_new_driver() from BaseCase."""
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--disable-3d-apis")
        options.add_argument("--disable-notifications")
        options.add_argument("--lang=en")
        if self.headless:
            options.add_argument("--headless=new")
            options.add_argument("--enable-gpu")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"],
        )
        prefs = {
            "translate_whitelists": {"ja": "en"},
            "translate": {"enabled": "true"}
        }
        options.add_experimental_option("prefs", prefs)
        return webdriver.Chrome(options=options)
    
    def test_simple(self):
        self.demo_mode = True
        self.open("https://townwork-net.translate.goog/joSrchRsltList?lcb=320112&sc=06668&_x_tr_sl=ja&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp")
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.scroll_to_element(".TM-adnetJobCassette__inner")
        elements = self.find_elements(".TM-adnetJobCassette.js-recordJobSeenCassette")
        
        jobs = []
        for element in elements:
            #print(element)
            type_of_job = element.find_element("css selector", ".TM-adnetJobCassette__tag").text
            company_name = element.find_element("css selector", ".TM-adnetJobCassette__company").text
            job_title = element.find_element("css selector", ".TM-adnetJobCassette__jobTtl").text
            
            miscellaneous = element.find_elements("css selector", ".TM-adnetJobCassette__recruitInfoTbl--txt")
            salary = miscellaneous[0].text
            traffic = miscellaneous[1].text
            working_hours = miscellaneous[2].text

            image_url_class = element.find_element("css selector", ".TM-adnetJobCassette__imgDetail--main")
            image_url = image_url_class.get_attribute("src")
            
            detailed_url_class = element.find_element("css selector", ".TM-adnetJobCassette__link")
            detailed_url = detailed_url_class.get_attribute('href')
            
            job = Job(type_of_job, company_name, job_title, salary, traffic, working_hours, detailed_url, image_url)
            print(job)
            jobs.append(job)
        
        # Move outside the loop to print all jobs
        

        # Return jobs list after all jobs are collected
        return jobs


override = OverrideDriverTest()
job_list = override.test_simple

    # Now you can get the length of the job_list
print(job_list)