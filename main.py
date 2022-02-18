from data_collection_manager import data_collection

from selenium import webdriver
from article import articleScrapObject
import os


os.environ['PATH'] += r"C:/chromedriver"

dc = data_collection(folder_name='test')

print(dc.find_string('wild fruits and'))