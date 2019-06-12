from requests.auth import HTTPBasicAuth
from .utils.constants import WEBHOOK, ME, ECHO
from .utils.requests import CaRequest


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
        return response

    def list_webhooks(self):
        response = self.request.get(WEBHOOK)
        return response

    def remove_webhook(self, id):
        response = self.request.delete(f'{WEBHOOK}/{id}')
        return response

    def get_webhook(self, id):
        response = self.request.get(f'{WEBHOOK}/{id}')
        return response

    def about(self):
        response = self.request.get(ME)
        return response

    def event_types(self):
        response = self.request.get(f'{ME}/event_types')
        return response

    def echo(self):
        response = self.request.get(ECHO)
        return response

