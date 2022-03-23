# Download the helper library from https://www.twilio.com/docs/python/install
from multiprocessing.spawn import import_main_path
import os
import urllib

import twilio
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid=os.environ['TWILIO_ACCOUNT_SID']='xuhxyxiuyh;kasdwad'
auth_token=os.environ['TWILIO_AUTH_TOKEN']='hlasjkcjksbcs'
client = Client(account_sid, auth_token)

"""
client = Client(account_sid, auth_token)
try:
    client.api.account.messages.create(
        to="+4874873974",
        from_="+17069325870",
        body="Hello there!")
except twilio.TwilioException as ex:
    print(ex)"""

link = "https://bit.ly/36n1O1X"
message = client.messages.create(
                               body=" Hi there Dania folk! If you want to be smarter everyday, access the brain quiz shorturl.at/nqAZ8 and you will see a nice tailored picture just for you. I will see you there!! ",
                               from_='+17069325870',
                                to='+86896034852'
                                 )

print(message.sid)
