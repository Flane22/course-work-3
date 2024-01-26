import requests, json


def get_list_from_url(url: str):
    result = requests.get(url)
    return result.json()


def get_list_from_file(path: str):
    with open(path, encoding="utf8") as f:
        return json.load(f)
