from article import articleScrapObject
import json
import glob
import os


def json_file_name_to_url(link: str):
    name_to_urk = 'https://' + link.replace('_', '/').replace('.json', '')
    return name_to_urk


def usable_link_to_file_name(link: str):
    link_to_file_name = link.replace('https://', '').replace('/', '_')
    return link_to_file_name

def data_dict_to_object_list(data_list):

    object_list = []

    for data in data_list:
        new_object = articleScrapObject()
        new_object.set_link(data)
        new_object.set_body(data_list[data]['body'])
        new_object.set_title(data_list[data]['title'])
        object_list.append(new_object)

    return object_list

def load_files_in_folder_list(folder_name):
    data_dict = {}
    articles_files = list(glob.glob(f"{folder_name}/" + "*"))
    file_names = ['https://' + os.path.basename(x).replace('.json', '').replace('_', '/') for x in articles_files]
    for article_file in articles_files:
        with open(f'{article_file}', 'rb') as file_obj:
            data = json.load(file_obj)
            key = list(data.keys())[0]
            data_dict[key] = {'title' : data[key]['title'], 'body' : data[key]['body']}
    return data_dict

def get_link_in_folder(folder_name):
    articles_files = list(glob.glob(f"{folder_name}/" + "*"))
    file_names = ['https://' + os.path.basename(x).replace('.json', '').replace('_', '/') for x in articles_files]
    return file_names

def load_file(data):
    link = articleScrapObject.get_link()
    file_name = usable_link_to_file_name(link)
    with open(f'{file_name}.json', 'rb') as file_obj:
        data = json.load(file_obj)
    return data


def save_file(articleScrapObject,folder_name):
    link = articleScrapObject.get_link()
    file_name = usable_link_to_file_name(link)
    data_dict = {link: {'body': articleScrapObject.get_body(), 'title': articleScrapObject.get_title()}}
    with open(f'{folder_name}/{file_name}.json', 'w') as file_obj:
        json.dump(data_dict, file_obj)
