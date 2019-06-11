from calendly_client import calendly

def test_about(fake_about):
    api_key = '123abc'
    c = calendly(api_key)
    r = c.about()
    assert r.status_code == 200


def test_echo(fake_echo):
    api_key = '123abc'
    c = calendly(api_key)
    r = c.echo()
    assert r.status_code == 200
    assert 'email' in r.json()


def test_event_types(fake_events_type):
    api_key = '123abc'
    c = calendly(api_key)
    r = c.event_types()
    assert r.status_code == 200
    assert 'type' in r.json()['data'][0]


def test_get_webhook(fake_get_webhook):
    id = '1234'
    api_key = '123abc'
    c = calendly(api_key)
    r = c.get_webhook(id)
    assert r.status_code == 200
    assert r.json()['data'][0]['id'] == id


def test_list_webhooks(fake_get_webhook):
    api_key = '123abc'
    c = calendly(api_key)
    r = c.list_webhooks()
    assert r.status_code == 200


def test_create_webhook(fake_create_webhook):
    api_key = '123abc'
    c = calendly(api_key)
    r = c.create_webhook('https://test.com')
    assert r.status_code == 200


def test_remove_webhook(fake_requests):
    fake_requests()
    api_key = '123abc'
    c = calendly(api_key)
    r = c.remove_webhook('1234')
    assert r.status_code == 200

