import os
import json


def save_json(path, obj):
    with open(path+'tmp', 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    os.rename(path+'tmp', path)


def load_json(path):
    with open(path, 'r') as f:
        obj = json.load(f)
    return obj


class AppData(object):

    def __init__(self, page_class, auto_process=True):
        self.page_class = page_class

        if auto_process:
            pass


def get_app_data(page_class):
    return AppData(page_class)
