from utils.http_requests import Request


class BaseController:
    def __init__(self, base_url):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = base_url
        self.request = Request()
