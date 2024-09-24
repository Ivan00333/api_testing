import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


LIST_ALL_SUB_BREEDS = [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"]

afghan_file_path = os.path.join(BASE_DIR, 'files', 'afgain_list.json')
with open(afghan_file_path, 'r') as file:
        LIST_BREEDS_IMAGES_AFGHAN = json.load(file)

basset_file_path = os.path.join(BASE_DIR, 'files', 'basset_list.json')
with open(basset_file_path, 'r') as file_basset:
        LIST_BREEDS_IMAGES_BASSET = json.load(file_basset)

blood_file_path = os.path.join(BASE_DIR, 'files', 'blood_list.json')
with open(blood_file_path, 'r') as file_blood:
        LIST_BREEDS_IMAGES_BLOOD = json.load(file_blood)

english_file_path = os.path.join(BASE_DIR, 'files', 'english_list.json')
with open(english_file_path, 'r') as file_basset:
        LIST_BREEDS_IMAGES_ENGLISH = json.load(file_basset)

ibizan_file_path = os.path.join(BASE_DIR, 'files', 'ibizan_list.json')
with open(ibizan_file_path, 'r') as file_basset:
        LIST_BREEDS_IMAGES_IBIZAN = json.load(file_basset)

plott_file_path = os.path.join(BASE_DIR, 'files', 'plott_list.json')
with open(plott_file_path, 'r') as file_basset:
        LIST_BREEDS_IMAGES_PLOTT = json.load(file_basset)

walker_file_path = os.path.join(BASE_DIR, 'files', 'walker_list.json')
with open(walker_file_path, 'r') as file_basset:
        LIST_BREEDS_IMAGES_WALKER = json.load(file_basset)