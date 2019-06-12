import pytest
import json
from ..calendly import Calendly


about_me_payload = {
  "data":{
    "type":"users",
    "id":"XXXXXXXXXXXXXXXX",
    "attributes":{
      "name":"Jane Doe",
      "slug":"janedoe",
      "email":"janedoe30305@gmail.com",
      "url":"https://calendly.com/janedoe",
      "timezone":"America/New_York",
      "avatar":{
        "url":"https://d3v0px0pttie1i.cloudfront.net/uploads/user/avatar/68272/78fb9f5e.jpg"
      },
      "created_at":"2015-06-16T18:46:52Z",
      "updated_at":"2016-08-23T19:40:07Z"
    }
  }
}

echo_payload = {
  'email': 'test@example.com'
}

events_types_payload = {
  "data":[
    {
      "type":"event_types",
      "id":"AAAAAAAAAAAAAAAA",
      "attributes":{
        "name":"15 Minute Meeting",
        "description":"",
        "duration":30,
        "slug":"15min",
        "color":"#fff200",
        "active":True,
        "created_at":"2015-06-16T18:46:53Z",
        "updated_at":"2016-08-23T19:27:52Z",
        "url":"https://calendly.com/janedoe/15min"
      }
    },
    {
      "type":"event_types",
      "id":"BBBBBBBBBBBBBBBB",
      "attributes":{
        "name":"30 Minute Meeting",
        "description":"",
        "duration":30,
        "slug":"30min",
        "color":"#74daed",
        "active":True,
        "created_at":"2015-06-16T18:46:53Z",
        "updated_at":"2016-06-02T16:26:44Z",
        "url":"https://calendly.com/janedoe/30min"
      }
    },
    {
      "type":"event_types",
      "id":"CCCCCCCCCCCCCCCC",
      "attributes":{
        "name":"Sales call",
        "description":None,
        "duration":30,
        "slug":"sales-call",
        "color":"#c5c1ff",
        "active":False,
        "created_at":"2016-06-23T20:13:17Z",
        "updated_at":"2016-06-23T20:13:22Z",
        "url":"https://calendly.com/acme-team/sales-call"
      }
    }
  ]
}

webhook_id = { 
    'id': '1234'
}


def single_webhook_payload(id):
    return {
          "type":"hooks",
          "id":id,
          "attributes":{
            "url":"http://foo.bar/1",
            "created_at":"2016-08-23T19:15:24Z",
            "state":"active",
            "events":[
              "invitee.created",
              "invitee.canceled"
            ]
          }
        }


def get_webhook_payload(ids=[1234]):
    response = {
      "data":[
          single_webhook_payload(id) for id in ids 
      ]
    }
    return response


def get_response(payload):
    class Data:
        status_code = 200
        text = json.dumps(payload)

        def json(self):
            return payload
    return Data()


@pytest.fixture
def fake_requests(monkeypatch):
    def method_payload(payload={}):
        def fake_method(url, json, headers):
            return get_response(payload)

        monkeypatch.setattr('requests.get', fake_method)
        monkeypatch.setattr('requests.post', fake_method)
        monkeypatch.setattr('requests.delete', fake_method)
    return method_payload


@pytest.fixture
def fake_about(fake_requests):
    return fake_requests(about_me_payload)


@pytest.fixture
def fake_echo(fake_requests):
    return fake_requests(echo_payload)


@pytest.fixture
def fake_events_type(fake_requests):
    return fake_requests(events_types_payload)


@pytest.fixture
def fake_get_webhook(monkeypatch):
    def fake_get(url, json, headers):
        id = url.split('/')[-1]
        ids = ['1234', '12345'] if id == 'hooks' else [id]
        payload = get_webhook_payload(ids)
        return get_response(payload)
    monkeypatch.setattr('requests.get', fake_get)


@pytest.fixture
def fake_create_webhook(fake_requests):
    return fake_requests(webhook_id)


@pytest.fixture
def calendly_client():
    api_key = '123abc'
    return Calendly(api_key)
    
