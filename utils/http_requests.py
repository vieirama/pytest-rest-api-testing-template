import requests
import json
from dataclasses import dataclass
from types import SimpleNamespace

@dataclass
class Response:
    status_code: int
    headers: dict
    json: object
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
        status_code = response.status_code
        headers = response.headers
        
        try:
            response_json = response.json()
            obj = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
        except Exception:
            response_json = {}
            obj = SimpleNamespace()
        
        return Response(status_code, headers, response_json, obj)
