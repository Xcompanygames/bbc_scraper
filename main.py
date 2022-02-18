from data_collection_manager import data_collection
import os


os.environ['PATH'] += r"C:/chromedriver"

dc = data_collection(folder_name='test')

print(dc.find_string('wild fruits and'))

dc.close_driver()
