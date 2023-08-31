import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from lets.letters import LETTERS


class WordScraperBot:
    driver_path = '.\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = self._setup_driver()
        self.base_url = 'https://www.webonary.org/balochidictionary/browse/browse-vernacular/?key=bcc&letter={}'
        self.connect_to_database()
    
    def run(self):
        sleep(4)
        self.create_table()
        self.letter = input('Enter a letter: ')
        self.driver.get(self.base_url.format(self.letter))
        self.scrape_pages()

        self.conn.close()


    def _setup_driver(self):
        driver = webdriver.Chrome(service=Service(executable_path=self.driver_path))
        return driver


    def connect_to_database(self):
        self.conn = sqlite3.connect('word_data.db')
        self.cursor = self.conn.cursor()
        print('Connected to db.')
        

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS word_data (
                letter TEXT,
                balochi TEXT,
                latin TEXT,
                definitions TEXT
            )
        ''')
        
        self.conn.commit()


    def insert_data(self, balochi, latin, definitions):
        self.cursor.execute('''
            INSERT INTO word_data (letter, balochi, latin, definitions)
            VALUES (?, ?, ?, ?)
        ''', (self.letter, balochi, latin, ', '.join(definitions)))

        self.conn.commit()


    def scrape_pages(self):
        while True:
            self.extract_data_from_current_page()
            
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, 'li.active_page + li a')
                if 'disabled' in next_button.get_attribute('class'):
                    break
                next_button.click()
                sleep(2)
            except:
                print('ERROR: NO SUCH ELEMENT1')
                self.driver.quit()
                break
                

    def extract_data_from_current_page(self):
        entry_elements = self.driver.find_elements(By.CLASS_NAME, 'entry')
        for entry_element in entry_elements:
            balochi = entry_element.find_element(By.CSS_SELECTOR, 'span[lang="bcc"]').text
            latin = entry_element.find_element(By.CSS_SELECTOR, 'span[lang="bcc-Latn-x-com"]').text

            definition_elements = entry_element.find_elements(By.CSS_SELECTOR, '.sensecontent .definition span[lang="en"]')
            definitions = [def_element.text for def_element in definition_elements]

            print("balochi:", balochi)
            print("latin:", latin)
            print("Definitions:", definitions)
            print("\n")

            self.insert_data(balochi, latin, definitions)
            sleep(0.4)