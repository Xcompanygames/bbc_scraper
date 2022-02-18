import time
from linkscraperobject import linkScraperObject
from article import articleScrapObject
import os
import glob
import file_manager
from selenium import webdriver
from tqdm import tqdm


class data_collection:
    def __init__(self, folder_name):
        self.driver = webdriver.Chrome()
        # Folder to save all articles
        self.folder_name = folder_name
        # Create article folder
        self.create_new_folder()
        # Load data
        # Load links in folder
        self.links_in_folder = file_manager.get_link_in_folder(self.folder_name)
        # Load dict and list of object
        self.article_dict = file_manager.load_files_in_folder_list(self.folder_name)
        self.article_list = file_manager.data_dict_to_object_list(self.article_dict)

        # Getting link from BBC site
        self.new_article_links = self.link_initiation()

        # Updating link according to what already scraped
        self.link_update()
        self.new_article_list = []
        # Initiating scraping from BBC
        self.article_collection_initiation()
        # Saving scraped data
        self.save_new_articles()
        # Combined article lists
        self.combined_articles = self.new_article_list + self.article_list

    def save_new_articles(self):
        for article in self.new_article_list:
            file_manager.save_file(article, self.folder_name)

    def link_initiation(self):
        ls = linkScraperObject(self.folder_name)
        return ls.get_links()

    def link_update(self):
        """
        Get new links to scrape and already scraped sites
        :return: new links without ones that already scraped
        """

        for link in self.new_article_links:
            if link in self.links_in_folder:
                self.new_article_links.remove(link)

    def create_new_folder(self):
        if not os.path.isdir(self.folder_name):
            os.mkdir(self.folder_name)

    def article_collection_initiation(self):
        for link in tqdm(self.new_article_links):
            scraper = articleScrapObject(self.driver, link)
            scraper.initiate_all()
            self.new_article_list.append(scraper)
            time.sleep(1)

    def find_string(self, string_to_find):
        for article in self.combined_articles:
            if article.find_string_in_article(string_to_find):
                return article.get_link()
        return 'Did not find string in articles'

    def get_article_dict(self):
        return self.new_articles_as_dict

    def get_article_links(self):
        return self.new_article_links
