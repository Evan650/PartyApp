import json
from twilio.rest import TwilioRestClient



people_json = {
    "people": [
        {
            "number": "7204125686",
            "fname": "Evan",
            "lname": "Yin",
            "location": "Boulder"
        },
        {
            "number": "7202916454",
            "fname": "Kenny",
            "lname": "Ellis",
            "location": "Boulder"
        },
        {
            "number": "7209389660",
            "fname": "Angela",
            "lname": "Werner",
            "location": "Boulder"
        }
    ]
}
parsed_json=json.dumps(people_json)

print(people_json.people.number)




# client = TwilioRestClient(account='AC1886dcb01585fe153b03644681df3ef4',
#                               token='732134a0980da87ca9b621b96966f085')

# client.messages.create(from_= "(720) 709-2497",
# 			to = people.kenny_number,
# 			body = "Fuck You")


