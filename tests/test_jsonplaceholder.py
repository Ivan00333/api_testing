import json

import pytest
import random
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from constants import UrlsJsonplaceholder
from lib.schemas.jsonplaceholder_schema import JsonplaceholderSchema, JsonplaceholderListing

class TestJsonplaceholder(BaseCase):

    list_names = ['userId', 'id', 'title', 'body']
    @pytest.mark.parametrize('id', [1, 2, 10])
    def test_get_resource_by_id(self, id):
        response = MyRequests.get(f"{UrlsJsonplaceholder.BASE_URL}/{id}")

        Assertions.check_schema(response, JsonplaceholderSchema)
        Assertions.check_response(
            response,
            status_code=200,
            list_names=self.list_names,
            name='id',
            expected_value=id
        )

    def test_create_resource(self):
        payload = {
            "title": f"test_{random.randint(1, 1000)}",
            "body": f"test_body_{random.randint(1, 1000)}",
            "userId": random.randint(1, 100)
            }

        headers = {
                'Content-type': 'application/json; charset=UTF-8',
              }

        response = MyRequests.post(UrlsJsonplaceholder.BASE_URL, json=payload, headers=headers)
        response_as_dict = response.json()

        Assertions.check_status_code_and_schema(response, JsonplaceholderSchema, 201)
        Assertions.assert_json_value_by_name(response, 'title', payload["title"])
        Assertions.assert_json_value_by_name(response, 'body', payload["body"])
        Assertions.assert_json_value_by_name(response, 'userId', payload["userId"])

    def test_delete_resource(self):
        response = MyRequests.delete(f"{UrlsJsonplaceholder.BASE_URL}/1")

        Assertions.assert_status_code(response,200)

    @pytest.mark.parametrize('user_id', [1, 5])
    def test_filter_by_user_id(self, user_id):
        response = MyRequests.get(f"{UrlsJsonplaceholder.BASE_URL}?userId={user_id}")
        response_data = response.json()

        assert len(response_data) > 0, f"Response is empty for userId={user_id}"
        Assertions.check_schema(response, JsonplaceholderSchema)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, 'userId', user_id)
        Assertions.assert_json_has_keys(response, self.list_names)

    @pytest.mark.parametrize('post_id', [1, 2])
    def test_listing_resourses(self, post_id):
        response = MyRequests.get(f"{UrlsJsonplaceholder.BASE_URL}/{post_id}/comments")

        Assertions.check_status_code_and_schema(response, schema=JsonplaceholderListing, status_code=200)
        Assertions.assert_json_value_by_name(response, "postId", post_id)