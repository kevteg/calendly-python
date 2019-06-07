from requests.auth import HTTPBasicAuth
from utils.constants import WEBHOOK_URL
from utils.requests import CaRequest


class calendly(object):

    event_types_def = {
        "canceled": "invitee.canceled",
        "created": "invitee.created"
    }

    def init(api_key):
        self.auth = self._auth(api_key)
        self.requests = CaRequest(self.auth)

    def _auth(api_key):
         return HTTPBasicAuth(api_key, '')
    
    def create_webhook(user_url, event_types=["canceled", "created"]):
        events = [self.event_types_def[event_type] for event_type in event_types]
        data = {'url': user_url, 'events': events}
        response = self.request.post(WEBHOOK_URL, data)
        return response
