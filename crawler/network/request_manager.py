import requests
from crawler.network.request_data_manager import RequestReturnData

class RequestManager:
    def __init__(self):
        pass

    def request(self, tag, url, callback, **kwargs):
        response = requests.get(url)
        callback(RequestReturnData(url, response.text))
