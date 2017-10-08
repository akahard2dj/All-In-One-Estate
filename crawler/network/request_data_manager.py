class RequestReturnData:
    def __init__(self, url, html):
        #self._index = index
        self._url = url
        self._html = html
        #self._sub_list = sub_list

    def get_html(self):
        return self._html

    def get_url(self):
        return self._url

'''
    def get_index(self):
        return self._index

    def get_sub_list(self):
        return self._sub_list
'''