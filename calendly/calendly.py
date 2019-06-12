from requests.auth import HTTPBasicAuth
from json import JSONDecodeError
from calendly.utils.constants import WEBHOOK, ME, ECHO
from calendly.utils.requests import CaRequest


class Calendly(object):

    event_types_def = {
        "canceled": "invitee.canceled",
        "created": "invitee.created"
    }

    def __init__(self, api_key):
        self.request = CaRequest(api_key)

    def create_webhook(self, user_url, event_types=["canceled", "created"]):
        events = [self.event_types_def[event_type] for event_type in event_types]
        data = {'url': user_url, 'events': events}
        response = self.request.post(WEBHOOK, data)
        return response.json()

    def list_webhooks(self):
        response = self.request.get(WEBHOOK)
        return response.json()

    def remove_webhook(self, id):
        dict_response = {'success': True}
        response = self.request.delete(f'{WEBHOOK}/{id}')
        dict_response['success'] = response.status_code == 200
        try:
            json_response = response.json()
        except JSONDecodeError:
            json_response = {}
        dict_response.update(json_response)
        return dict_response

    def get_webhook(self, id):
        response = self.request.get(f'{WEBHOOK}/{id}')
        return response.json()

    def about(self):
        response = self.request.get(ME)
        return response.json()

    def event_types(self):
        response = self.request.get(f'{ME}/event_types')
        return response.json()

    def echo(self):
        response = self.request.get(ECHO)
        return response.json()

