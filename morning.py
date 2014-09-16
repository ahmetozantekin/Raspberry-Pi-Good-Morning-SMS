#!/usr/bin/env python

import urllib, json
from xml.dom import minidom
from twilio.rest import TwilioRestClient
account_sid = "YOUR TWILIO SID"
auth_token = "YOUR TWILIO AUTH TOKEN"
client = TwilioRestClient(account_sid, auth_token)
 
wurl = 'http://xml.weather.yahoo.com/forecastrss?p=%s' # weather rss
wser = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def bitcoin_price():
    coinbaseURL = 'https://coinbase.com/api/v1/prices/sell'
    coinbaseResponse = urllib.urlopen(coinbaseURL);
    data = json.loads(coinbaseResponse.read())
    return "Good morning, Chase. The current Bitcoin price is $" + data["amount"] + "."

def weather_for_zip(zip_code):
    url = wurl % zip_code +'&u=f'
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(wser, 'forecast'):
        forecasts.append({           
            'high': node.getAttribute('high'), # gets high temperature attribute
        })
    ycondition = dom.getElementsByTagNameNS(wser, 'condition')[0]
    return {
        'forecasts': forecasts ,
        'title': dom.getElementsByTagName('title')[0].firstChild.data
    }
ZIP = 'YOUR ZIP CODE'
TO = 'YOUR PHONE NUMBER'
FROM = 'YOUR TWILIO NUMBER'
 
a = weather_for_zip(ZIP)
hight = a['forecasts'][0]['high'] # Defines hight as the high temperature
temp = int(hight)
message1Body = ''
message2Body = ''

if temp < 65: # The sixty and the other numbers can be changed to user's preferences.
    message1Body = "I recommend wearing something slightly warm... It is only " + str(temp) + " degrees!"
    message2Body = "May I suggest a hoodie?"
elif temp >= 65 and temp < 85:
    message1Body = "It's going to be warm today at " + str(temp) + " degrees!"
    message2Body = "I suggest wearing a button down shirt with your black jeans!"
else:
    message1Body = "It's going to be hot today at " + str(temp) + " degrees!"
    message2Body = "Perhaps a t-shirt and shorts will suffice?"

client.messages.create(body=bitcoin_price(), to=TO, from_ = FROM)
client.messages.create(body=message1Body, to=TO, from_ = FROM)
client.messages.create(body=message2Body, to=TO, from_ = FROM)