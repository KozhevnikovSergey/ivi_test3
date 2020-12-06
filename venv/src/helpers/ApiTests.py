import json

import requests


class SessionApi:

    _session_authorized = None

    @classmethod
    def get_authorized(cls, login, password):
        if not cls._session_authorized:
            cls._session_authorized = requests.Session()
            cls._session_authorized.auth = (login, password)
        return cls._session_authorized


class ApiTests:
    session_authorized = None
    URL = "http://rest.test.ivi.ru/v2"

    def get_result(self, response):
        new_r = json.loads(response.text)
        result = new_r.get('result')
        assert result, "В ответе отсутсвует result"
        return result

