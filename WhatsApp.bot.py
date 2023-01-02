import os
from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello, world!',
    to='whatsapp:+1234567890'
)

print(message.sid)
