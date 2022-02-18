from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class articleScrapObject:
    def __init__(self, driver=None, url=None):
        self.body = ''
        self.title = ''
        self.link = url
        self.driver = driver

    def close_driver(self):
        self.driver.close()

    def initiate_drive(self):
        time.sleep(1)
        self.driver.get(self.link)
        time.sleep(1)

    def initiate_body(self) -> list:
        # Collect all paragraphs
        article_content = self.driver.find_elements(By.CSS_SELECTOR, "p")
        # Filter href, and span from paragraphs
        time.sleep(0.5)
        filter_tags_1 = [article for article in article_content if
                         'span' not in article.get_attribute("innerHTML") and 'href' not in article.get_attribute(
                             "innerHTML")]
        # Filter texts by tags if parent containing them
        filter_tags_2 = [article for article in filter_tags_1 if
                         'href' not in article.find_element(By.XPATH, "..").get_attribute("innerHTML")]
        # Get text
        body = [article.get_attribute("textContent") for article in filter_tags_2]
        return body

    def initiate_title(self) -> str:

        title_0 = self.driver.find_elements(By.CLASS_NAME, "lx-c-session-header-content__event-info qa-event-header-wrap")
        if len(title_0) > 0:
            return title_0[0].get_attribute("textContent")
        title_1 = self.driver.find_elements(By.ID, "main-heading")
        if len(title_1) > 0:
            return title_1[0].get_attribute("textContent")
        title_2 = self.driver.find_elements(By.XPATH, "//div[@tabindex='-1']")
        if len(title_2) > 0:
            return title_2[0].get_attribute("textContent")
        title_3 = self.driver.find_elements(By.ID, "lx-event-title")
        if len(title_3) > 0:
            return title_3[0].get_attribute("textContent")
        title_4 = self.driver.find_elements(By.CLASS_NAME, "vj-header__headline")
        if len(title_4) > 0:
            return title_4[0].get_attribute("textContent")

    def find_string_in_article(self, str_to_search):
        for sentence in self.get_body():
            if str_to_search in sentence:
                return True
        return False

    def initiate_all(self):
        self.initiate_drive()
        self.title = self.initiate_title()
        self.body = self.initiate_body()

    def get_body(self):
        return self.body

    def get_title(self):
        return self.title

    def get_link(self):
        return self.link

    def set_body(self, body):
        self.body = body

    def set_title(self, title):
        self.title = title

    def set_link(self, link):
        self.link = link
