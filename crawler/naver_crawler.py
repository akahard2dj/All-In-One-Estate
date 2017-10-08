import requests
import logging
from bs4 import BeautifulSoup

from crawler.network.web_crawler import WebCrawler
from crawler.network.request_data_manager import RequestReturnData


class NaverCrawlerC1(WebCrawler):
    def __init__(self):
        WebCrawler.__init__(self)

    def request(self):
        self.rm.request('Naver_C1', 'http://land.naver.com/', self.callback)

    def callback(self, data: RequestReturnData):
        self.parse(data)

    def parse(self, data: RequestReturnData):
        text = data.get_html()

        soup = BeautifulSoup(text, "html.parser")
        select_box = soup.find("select", {"class": "selectbox-source"})
        option_lists = select_box.findAll("option")

        for index, option in enumerate(option_lists):
            item = dict()
            item['c1_code'] = option['value']
            item['c1_mapx'] = option['xcrdn']
            item['c1_mapy'] = option['ycrdn']
            item['c1_name'] = option.text

