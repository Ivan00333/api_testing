import enum
import json


class UrlsDogApi(enum.auto):

    BASE_URL = 'https://dog.ceo/api/breed/hound/'

    URL_LIST_ALL_SUB_BREEDS = f'{BASE_URL}list'
    URL_GET_IMAGE_RANDOM = f"{BASE_URL}images/random"

class UrlsOpenBrewery(enum.auto):

    BASE_URL = 'https://api.openbrewerydb.org/v1/breweries/'



