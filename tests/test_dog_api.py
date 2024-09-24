import pytest
from lib.my_requests import MyRequests
from constants import Urls
from lib.assertions import Assertions
from lib.dog_data import LIST_ALL_SUB_BREEDS

class TestDogApi:

    def test_list_all_sub_breeds(self):
        response = MyRequests.get(Urls.URL_LIST_ALL_SUB_BREEDS)
        message = response.json()['message']

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_keys(response, ['message', 'status'])
        Assertions.assert_json_value_by_name(response, "status", "success")

        if len(LIST_ALL_SUB_BREEDS) == len(message):
            for i in LIST_ALL_SUB_BREEDS:
                assert i in message, f"{i} not in the list {message}"
        else:
            raise ValueError(f"Expected {len(LIST_ALL_SUB_BREEDS)} items, but got {len(message)}")

    @pytest.mark.parametrize('breed', LIST_ALL_SUB_BREEDS)
    def test_list_all_sub_breeds_images(self, breed):
        response = MyRequests.get(f"{Urls.BASE_URL}{breed}/images")
        print(response.url)