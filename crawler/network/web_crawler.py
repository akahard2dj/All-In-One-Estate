import time
from crawler.network.request_manager import RequestManager
from crawler.network.request_data_manager import RequestReturnData


class WebCrawler:
    def __init__(self):
        self.code = list()
        self.rm = RequestManager()

    def request(self):
        raise NotImplementedError

    def parse(self, data: RequestReturnData):
        raise NotImplementedError

    def callback(self, data: RequestReturnData):
        raise NotImplementedError

    def result(self):
        return self.code
