# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC9d24390d2bc5a3da60fe9d4175f66234"
# auth_token = os.environ["27affabbdd0f04a854956ec4b0d9093d"]
client = Client(account_sid, '27affabbdd0f04a854956ec4b0d9093d')

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+919810576763",
  from_="+15855493995"
)

print(call.sid)