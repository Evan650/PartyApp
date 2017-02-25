import json
from twilio.rest import TwilioRestClient

json_data=open("data.json").read()


client = TwilioRestClient(account='AC1886dcb01585fe153b03644681df3ef4',
                              token='732134a0980da87ca9b621b96966f085')

client.messages.create(from_= "(720) 709-2497",
			to = people.kenny_number,
			body = "Fuck You")



