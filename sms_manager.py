import os
from twilio.rest import Client

# Twillio auth
ACC_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
MY_TWILLIO_NUM = os.environ['MY_TWILIO_NUM']
TWILIO_VERIFIED_NUM = os.environ['TWILIO_VERIFIED_NUM']


class SMSManager(): 
    def __init__(self) -> None:
        pass
    
    def send_msg(self) -> None:
        client = Client(ACC_SID, AUTH_TOKEN)
        message = client.messages \
                    .create(
                        body="It might rain so please remember to take an umbrella",
                        from_= MY_TWILLIO_NUM,
                        to= TWILIO_VERIFIED_NUM
                    )
        print(message.sid) # Message went through or not feedback