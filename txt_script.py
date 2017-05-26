from twilio.rest import Client
import os


if __name__ == '__main__':
    API_KEY = os.environ['TWILIO_API_KEY']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
            to="+13035165965",
            from_="+17205525069",
            body="Hello from Python!")

    print(message.sid)