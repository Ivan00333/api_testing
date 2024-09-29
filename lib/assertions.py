from pydantic import ValidationError
from requests import Response
import json
from lib.schemas.brewery_schema import BrewerySchema

class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, \
            f"Expected value is {expected_value}. Actual: {response_as_dict[name]}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list=None):
        if names is not None:
            try:
                response_as_dict = response.json()
            except json.JSONDecoder:
                assert False, f"Response is not in JSON format. Response text is '{response.text}'"

            for name in names:
                assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"


    @staticmethod
    def check_response(response, status_code: int, list_names: list=None, name: str=None, expected_value: str=None):
        Assertions.assert_status_code(response, status_code)
        Assertions.assert_json_has_keys(response, list_names)
        Assertions.assert_json_value_by_name(response, name, expected_value)

    @staticmethod
    def check_status_code_and_schema(response, schema, status_code: int):

        Assertions.assert_status_code(response, status_code)
        Assertions.check_schema(response, schema)

    @staticmethod
    def check_schema(response, schema):

        json_data = response.json()
        if isinstance(json_data, list):
            for brewery in json_data:
                try:
                    schema(**brewery)
                except ValidationError as e:
                    assert False, f"Response schema validation failed: {e}"
        else:
            try:
                schema(**json_data)
            except ValidationError as e:
                assert False, f"Response schema validation failed: {e}"
