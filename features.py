import requests
import json
from credentials import openweather_api_key,bot_token
def sendmessage(chatid, text):
    URL = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
    payload = {
        "text":text,
        "chat_id":chatid
        }
    resp = requests.post(URL,params = payload)


def weatherReport(chatid,msgtext):

    try:
        url1 = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(msgtext,openweather_api_key)
        response = requests.get(url1)
        # print(response.json())
        data = response.json() # getting the main dict block
        main = data['main']    # getting temperature
        temperature = main['temp']  # getting the humidity
        humidity = main['humidity']  # getting the pressure
        pressure = main['pressure']   # weather report
        report = data['weather']
        sendmessage(chatid,"""
                    Temperature: {} 
                    Humidity: {}
                    Pressure: {}
                    Weather Report:{}
                    """.format(temperature,humidity,pressure,report))

    except Exception as e:
        sendmessage(chatid,"""Sorry unable to process your request .
        Please check the spelling of your city name""")
        return "OK"


def instagram(chatid, msgtext):
    try:
        url = "https://instagram47.p.rapidapi.com/get_user_id"
        querystring = {"username":"{}".format(msgtext)}
        headers = {
            'x-rapidapi-host': 'instagram47.p.rapidapi.com',
            'x-rapidapi-key': '47aa2f3fb5mshaf39e9eb1e0edfep12058bjsn5bbbcdfea110'
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        data = response.json()
        userid = data['user_id']
        print(userid,"----------")

        # sendmessage(chatid,userid)
      

        url1 = "https://instagram47.p.rapidapi.com/user_followers"

        querystring1 = {"userid":"{}".format(userid)}
        response1 = requests.request("GET", url1, headers=headers, params=querystring1)

        print(response1.json())
        data1 = response1.json()
        count = data1['body']['count']
        print(count)
        sendmessage(chatid, count)




    except Exception as e:
        sendmessage(chatid,"Please check the username provided")
        return "OK"
    
