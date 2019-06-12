<a href="https://codeclimate.com/github/kevteg/calendly-python/maintainability"><img src="https://api.codeclimate.com/v1/badges/8d96f6b46f140f3d178b/maintainability" /></a> [![CircleCI](https://circleci.com/gh/kevteg/calendly-python/tree/master.svg?style=svg)](https://circleci.com/gh/kevteg/calendly-python/tree/master)
# calendly-python 🐍

Python package to use the [Calendly](http://calendly.com) API  🚀


## Installation

    pip install calendly

## Usage

### Set your Authentication token
See [Calendly docs](https://developer.calendly.com/docs/getting-your-authentication-token) to get your auth token

    from calendly import Calendly
    calendly = Calendly(api_key)

#### Test the auth token

	calendly.echo()

#### Webhooks
##### Create A Webhook Subscription

    calendly.create_webhook('https://your-webhook.com', events=['canceled', 'invited'])

 - **Note:** the `events` variable is a list 
 - **Note:** possible values are: `canceled` and `invited` 
 - **Note:** by default the `events` list contains the 2 possible values

##### Get Webhook Subscription

    calendly.get_webhook('webhook_id')

##### Get List of Webhook Subscriptions

    calendly.list_webhooks()

##### Delete Webhook Subscription

    calendly.remove_webhook('webhook_id')

- **Note**: the response will be `{'success': True}` if the webhook was successfully removed, otherwise it will be `{'success': False, "type": "calendly type", "message": "reason it failed"}`

#### User Event Types

    calendly.event_types()

#### About Me

    calendly.about()

#### Important
- **Note:** All the responses are dictionaries with the calendly response, except for the remove webhook method that also contains the `success` key. Check their [docs](https://developer.calendly.com/docs/) to know the possible responses!
