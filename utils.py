import json

from constants import JSON_DATA


def get_data_from_json():
    with open(JSON_DATA, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
