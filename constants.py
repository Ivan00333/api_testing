import enum
import json


class Urls(enum.auto):

    BASE_URL = 'https://dog.ceo/api/breed/hound/'

    URL_LIST_ALL_SUB_BREEDS = f'{BASE_URL}list'


