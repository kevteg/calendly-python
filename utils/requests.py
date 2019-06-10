import requests
import json


class CaRequest(object):

    def __init__(self, token):
        self.headers = {'X-TOKEN': token}

    def process_request(self, method, url, data=None):
        request_method = getattr(requests, method)
        return request_method(url, json=data, headers=self.headers)

    def get(self, url, data=None):
        return self.process_request('get', url, data)

    def post(self, url, data=None):
        return self.process_request('post', url, data)

    def delete(self, url, data=None):
        return self.process_request('delete', url, data)

    def put(self, url, data=None):
        return self.process_request('put', url, data)

