import requests
import json
from dataclasses import dataclass
from types import SimpleNamespace

@dataclass
class Response:
    status_code: int
    headers: dict
    response_json: str
    obj: SimpleNamespace
    

class Request:

    def get(self, url):
        response = requests.get(url)
        return self.__get_response(response)

    def post(self, url, headers, payload):
        response = requests.post(url, json=payload, headers=headers)
        return self.__get_response(response)

    def put(self, url, headers, payload):
        response = requests.put(url, json=payload, headers=headers)
        return self.__get_response(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_response(response)

    def __get_response(self, response):
        try:
            obj = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
            response_json = response.json()
        except Exception:
            obj = SimpleNamespace()
            response_json = {}
        
        return Response(response.status_code, response.headers, response_json, obj)
