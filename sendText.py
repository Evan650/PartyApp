import json
from twilio.rest import TwilioRestClient



people_json = {
    "people": [
        {
            "number": "7204125686",
            "fname": "Evan",
            "lname": "Yin",
            "location": "Boulder",
            "account": "",
            "token": ""
            
        },
        {
            "number": "7202916454",
            "fname": "Kenny",
            "lname": "Ellis",
            "location": "Boulder",
            "account": "AC1886dcb01585fe153b03644681df3ef4",
            "token": "732134a0980da87ca9b621b96966f085"
        },
        {
            "number": "7209389660",
            "fname": "Angela",
            "lname": "Werner",
            "location": "Boulder",
            "account": "AC5c0db887bf711406092b7b6b83b4be7f",
            "token": "9e0786b06b9a303d9a86868e596450f1"
            
        }
    ]
}



parsed_json=json.dumps(people_json)

#print(people_json["people"][1]["number"])

client_kenny = TwilioRestClient(people_json["people"][1]["account"], people_json["people"][1]["token"])
client_Angela = TwilioRestClient(people_json["people"][2]["account"], people_json["people"][2]["token"])
client_Evan = TwilioRestClient(people_json["people"][0]["account"], people_json["people"][0]["token"])


client_Kenny.messages.create(from_= "(720) 709-2497",
			to = people_json["people"][1]["number"],
 			body = "Sup")

client_Angela.messages.create(from_= "(720) 663-7925",
			to = people_json["people"][2]["number"],
 			body = "AYYYY")

client_Evan.messages.create(from_= "(720) 709-2497",
			to = people_json["people"][0]["number"],
 			body = "Yooo")
