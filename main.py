from weather import Weather
from sms_manager import SMSManager


# Instances
weather = Weather()
sms = SMSManager()

print(weather.will_rain())
# if it will rain today
if weather.will_rain():
    sms.send_msg()