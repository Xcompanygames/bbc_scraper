import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import glob

class linkScraperObject:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.bbc.com/')
        time.sleep(1)
        self.links = self.get_links()
        self.get_all_scraped_links()
    def close_driver(self):
        self.driver.close()

    def get_all_scraped_links(self):
        file_list = list(glob.glob(f"{self.folder_name}/"+ "*"))
        file_names = ['https://'+os.path.basename(x).replace('.json','').replace('_','/') for x in file_list]
        for file_name in file_names:
            if file_name in self.links:
                self.links.remove(file_name)

    def get_links(self) -> list:
        articles = self.driver.find_elements(By.CLASS_NAME, "block-link__overlay-link")
        #### Getting links from the main page
        links = [elem.get_attribute('href') for elem in articles]
        return links