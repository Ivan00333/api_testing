import json
import os
import pytest
from lib.my_requests import MyRequests
from constants import UrlsDogApi
from lib.assertions import Assertions
from lib.dog_data import LIST_ALL_SUB_BREEDS
from lib.base_case import BaseCase


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDogApi(BaseCase):

    def test_list_all_sub_breeds(self):
        response = MyRequests.get(UrlsDogApi.URL_LIST_ALL_SUB_BREEDS)
        message = self.get_json_value(response, "message")

        Assertions.check_response(
            response,
            status_code=200,
            list_names=['message', 'status'],
            name="status",
            expected_value="success"
        )

        assert set(LIST_ALL_SUB_BREEDS) == set(message), "List of sub-breeds doesn't not match"

    @pytest.mark.parametrize('breed', LIST_ALL_SUB_BREEDS)
    def test_list_all_sub_breeds_images(self, breed):
        response = MyRequests.get(f"{UrlsDogApi.BASE_URL}{breed}/images")

        Assertions.check_response(
            response,
            status_code=200,
            list_names=['message', 'status'],
            name="status",
            expected_value="success"
        )

        message_images = self.get_json_value(response, "message")
        file_path = os.path.join(BASE_DIR, 'files/dog_files', f"{breed}_list.json")

        with open(file_path, 'r') as file:
            expected_images = json.load(file)

        assert set(message_images) == set(expected_images), f"Images for breed {breed} do not match"

    def test_random_image(self):
        previous_message = None

        for r in range(3):
            response = MyRequests.get(UrlsDogApi.URL_GET_IMAGE_RANDOM)

            Assertions.check_response(
                response,
                status_code=200,
                list_names=['message', 'status'],
                name="status",
                expected_value="success"
            )

            current_message = self.get_json_value(response, "message")
            if previous_message is not None:
                assert current_message != previous_message, "Message in the response is the same as the previous one"

            previous_message = current_message

    @pytest.mark.parametrize('param', ['new', '02088094_1003', 'null'])
    def test_negative_sub_breed_image(self, param):
        response = MyRequests.get(f"{UrlsDogApi.BASE_URL}{param}/images")

        Assertions.check_response(
            response,
            status_code=404,
            list_names=['message', 'status', "code"],
            name="status",
            expected_value="error"
        )

        Assertions.assert_json_value_by_name(response,\
            "message", "Breed not found (sub breed does not exist)")

    @pytest.mark.parametrize('breed', LIST_ALL_SUB_BREEDS)
    @pytest.mark.parametrize('number', [1, 3, 10])
    def test_multiple_images(self, breed, number):
        response = MyRequests.get(f"{UrlsDogApi.BASE_URL}{breed}/images/random/{number}")
        message = self.get_json_value(response, "message")

        Assertions.check_response(
            response,
            status_code=200,
            list_names=['message', 'status'],
            name="status",
            expected_value="success"
        )
        if breed != 'plott':
            assert len(message) == number, \
                f"Number of images for sub-breed {breed} is {len(message)}, expected {number}"
        else:
            assert len(message) == number or len(message) == 2, \
                f"Number of images for sub-breed {breed} is {len(message)}, expected {number}"


