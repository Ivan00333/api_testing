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
            response_content = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        if isinstance(response_content, dict):

            assert name in response_content, f"Response JSON doesn't have key '{name}'"
            assert response_content[name] == expected_value, \
                f"Expected value is {expected_value}. Actual: {response_content[name]}"

        elif isinstance(response_content, list):
            for item in response_content:
                assert isinstance(item, dict), "List element is not a dictionary"
                if name in item:
                    assert item[name] == expected_value, \
                        f"Expected value is {expected_value}. Actual: {item[name]}"
                    return
            assert False, f"None of the list items contain the key '{name}'"
        else:
            assert False, "Response content is neither a JSON object nor a list of dictionaries"

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
                response_content = response.json()
            except json.JSONDecodeError:
                assert False, f"Response is not in JSON format. Response text is '{response.text}'"

            if isinstance(response_content, dict):
                for name in names:
                    assert name in response_content, f"Response JSON doesn't have key '{name}'"
            elif isinstance(response_content, list):
                for item in response_content:
                    assert isinstance(item, dict), "List element is not a dictionary"
                    for name in names:
                        assert name in item, f"One of the list items doesn't have key '{name}'"
            else:
                assert False, "Response content is neither a JSON object nor a list of dictionaries"


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
