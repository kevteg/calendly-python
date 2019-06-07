import requests
import json


class CaRequest(object):

    def __init__(auth):
        self.auth = auth

    def process_request(method, url, data=None, headers=None):
        #_ = {}
        #if data:
        #    _['data'] = json.dumps(kwargs["data"])

        request_method = getattr(requests, method)
        return request_method(url, data, auth=self.auth)

    def get(self, url, data=None):
        self.process_request('get', url, data)

    def post(self, url, data=None):
        self.process_request('post', url, data)

    def delete(self, url, data=None):
        self.process_request('delete', url, data)

    def put(self, url, data=None):
        self.process_request('put', url, data)

