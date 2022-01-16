import os
from dotenv import load_dotenv
from twilio.rest import Client

def SMS():
    load_dotenv()
    accountSid = os.getenv("TWILIO_ACCOUNT_SID")
    authToken = os.getenv("TWILIO_AUTH_TOKEN")

    client = Client(accountSid, authToken)

    client.messages.create(
        to=os.getenv("PHONETO"),
        from_=os.getenv("PHONEFROM"),
        body="Time to take a break! You deserve it!"
    )

