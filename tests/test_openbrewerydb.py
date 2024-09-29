import pytest
from lib.schemas.brewery_schema import BrewerySchema
from lib.openbrewery_data import LIST_BREWERIES, get_ids_breweries
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from constants import UrlsOpenBrewery


class TestOpenBrewery(BaseCase):

    def test_get_list_all_breweries(self):
        response = MyRequests.get(UrlsOpenBrewery.BASE_URL)

        Assertions.check_schema(response, BrewerySchema)

    @pytest.mark.parametrize('brewery_id', get_ids_breweries(LIST_BREWERIES))
    def test_get_brewery_by_id(self, brewery_id):
        response = MyRequests.get(f"{UrlsOpenBrewery.BASE_URL}/{brewery_id}")

        Assertions.check_status_code_and_schema(response, BrewerySchema, 200)

    @pytest.mark.parametrize('per_page', [1, 5, 10])
    def test_get_list_breweries_per_page(self, per_page):
        response = MyRequests.get(f"{UrlsOpenBrewery.BASE_URL}?per_page={per_page}")
        breweries_list = response.json()

        Assertions.check_status_code_and_schema(response, BrewerySchema, 200)
        assert len(breweries_list) == per_page, f"Expected number of breweries is {per_page}, actual is {len(breweries_list)} "