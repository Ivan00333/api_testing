import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

openbrewery_path = os.path.join(BASE_DIR, 'files/openbrewery_files', 'brewery_list.json')
with open(openbrewery_path, 'r') as file:
    LIST_BREWERIES = json.load(file)

def get_ids_breweries(list_breweries):
    return [brewery['id'] for brewery in list_breweries]