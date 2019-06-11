
def test_about(fake_about, calendly_client):
    r = calendly_client.about()
    assert r.status_code == 200
    assert r.json()['data']['type'] == 'users'


def test_echo(fake_echo, calendly_client):
    r = calendly_client.echo()
    assert r.status_code == 200
    assert 'email' in r.json()


def test_event_types(fake_events_type, calendly_client):
    r = calendly_client.event_types()
    assert r.status_code == 200
    assert 'type' in r.json()['data'][0]


def test_get_webhook(fake_get_webhook, calendly_client):
    id = '1234'
    r = calendly_client.get_webhook(id)
    assert r.status_code == 200
    assert r.json()['data'][0]['id'] == id


def test_list_webhooks(fake_get_webhook, calendly_client):
    r = calendly_client.list_webhooks()
    assert r.status_code == 200


def test_create_webhook(fake_create_webhook, calendly_client):
    r = calendly_client.create_webhook('https://test.com')
    assert r.status_code == 200


def test_remove_webhook(fake_requests, calendly_client):
    fake_requests()
    r = calendly_client.remove_webhook('1234')
    assert r.status_code == 200

