import requests
import os

from dotenv import load_dotenv
load_dotenv()

# Store credentials in .env file  
bot_token = os.environ.get("bot_token")
open_weatherApi_key = os.environ.get("open_weatherApi_key")
rapid_api_key = os.environ.get("rapid_api_key")

def sendmessage(chatid, text):
    URL = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
    payload = {
        "text" :text,
        "chat_id" : chatid
    }
    requests.get(URL, params=payload)


def weather(chatid, msgtext):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(msgtext,open_weatherApi_key)
        response = requests.get(url)
        # print(response.json())
        data = response.json()
        main = data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        sendmessage(chatid, """
            Temperature: {}
            Pressure: {}
            Humidity: {}""".format(temperature,pressure,humidity))
        return "OK"
        
    except Exception as e:
        sendmessage(chatid,"Sorry unable to process your request")
        return "OK"        
            



def instagram(chatid, msgtext):
    try:

        url = "https://instagram47.p.rapidapi.com/get_user_id"

        querystring = {"username":"{}".format(msgtext)}

        headers = {
            'x-rapidapi-host': "instagram47.p.rapidapi.com",
            'x-rapidapi-key': rapid_api_key
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # print(response.text)# get user id from response
        data = response.json()
        userid = data['user_id']
        print(userid,"--------------------------")
        sendmessage(chatid, "Please wait for a while")

        url1 = "https://instagram47.p.rapidapi.com/user_followers"

        querystring1 = {"userid":"{}".format(userid)}
        response = requests.request("GET", url1, headers=headers, params=querystring1)
        print(response.text)
        data1 = response.json()
        count = data1["body"]["count"]
        sendmessage(chatid, "{} has {} followers".format(msgtext,count))


    except Exception as e:
        sendmessage(chatid,"User not Found")
        return "OK"


def imdb (chatid, msgtext):
    try:
        url = "https://imdb8.p.rapidapi.com/auto-complete"

        querystring = {"q":"{}".format(msgtext)}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': rapid_api_key
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        # print(response.text)
        sendmessage(chatid,response.text)
        return "OK"
    except Exception as e:
        sendmessage(chatid, "Sorry unable to process your request")
        return "OK"

