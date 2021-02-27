api_key = '99d7e2f6a6a315052a452c51b130bea1'
params = {
    'lat':20.47,
    'lon':84.23,
    'exclude':'current,minutely,daily',
    'appid': api_key
}
account_sid = 'AC7e93521d8d195c41fd32dfb979621f2f'
auth_token = '0ebe13522df90237f154effc77ce33c8'
import requests
from twilio.rest import Client

will_rain = False
web_response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=params)
web_response.raise_for_status()
weather_data = web_response.json()
weather_slice_12 = weather_data['hourly'][:12]
for hour_data in weather_slice_12:
    cond_code =  hour_data['weather'][0]['id']
    if int(cond_code) < 700:
        will_rain = True
if will_rain:
    # print('Bring an umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Its raining today. Bring an umbrella",
                     from_='+17652759393',
                     to='+917978313039'
                 )
    print(message.sid)
# for hour in range(11):
#     print(weather_data['hourly'][hour]['weather'][0]['id'])

