from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import logging
from site_path import SITE_PATH




class WordScraperBot:

    def __init__(self):
        self.driver = self._setup_driver()
        self.driver_path = 'C:\Users\moawezz\Desktop\Upsaladic-Scrape\chromedriver\chromedriver.exe'
        self.url = 'https://www.webonary.org/balochidictionary/browse/browse-vernacular/?letter=%D8%A7%D9%93&key=bcc'
    
    def run(self):

        # Configure logging
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO)
        self.driver.get(self.url)
        

    def _setup_driver(self):
        logging.info('Setting Up driver.')
        # options = Options()
        # options.add_argument("--headless=new")  # run in headless mode (without gui)
        driver = webdriver.Chrome(service=Service(executable_path=self.driver_path))

        return driver
