from dotenv import load_dotenv
import requests
import os
from twilio.rest import Client

load_dotenv()


current_location_lat = 5.612942
current_location_lon = 5.863023

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
api_key = os.getenv("OWM_API_KEY")

weather_params = {
    "lat": 5.612934256300603,
    "lon": 5.8630226273733586,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(json.dumps(response, indent=4))

will_rain = False
counter = 0
for i in weather_data['list']:
    if weather_data['list'][counter]['weather'][0]['id'] < 700:
        print(weather_data['list'][counter]['weather'][0]['id'])
        will_rain = True
    counter += 1
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+16824185842', # Using SMS
        # from_='whatsapp:+14155238886', # Using WhatsApp
        body="It's going to rain today, remember to carry an ☂",
        to = '+2349036549273' # Using SMS
        # to='whatsapp:+2347057341712' # Using WhatsApp
    )
    print(message.sid)
    print(message.status)
