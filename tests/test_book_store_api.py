import requests
from Config import URL, URL_ISBN, BASE_URL
from jsonschema import validate
from src.schemas.post import POST_SCHEMA


class TestBookStore:

    def test_get_book(self):
        isbn = "9781449325862"
        params = "Book?ISBN="
        re = requests.get(BASE_URL + params + isbn)
        received_post = re.json()
        assert re.status_code == 200, 'Статус кода не соответствует'
        assert len(received_post) == 9, 'Колличество элементов не совпадает'
        validate(received_post, POST_SCHEMA)
