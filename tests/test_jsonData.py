from utils import jsonData

JSON_URL = "https://www.jsonkeeper.com/b/PLZ0"
JSON_PATH = "data/operations"


def test_get_list_from_file(result_from_json):
    assert jsonData.get_list_from_file(JSON_PATH)[0] == result_from_json


def test_get_list_from_url(result_from_json):
    assert jsonData.get_list_from_url(JSON_URL)[0] == result_from_json
