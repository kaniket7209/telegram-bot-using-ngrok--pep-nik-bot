from flask import Flask,request
import requests
import os
from dotenv import load_dotenv
load_dotenv()

from features import imdb, instagram, weather



# Store credentials in .env file  
bot_token = os.environ.get("bot_token")
open_weatherApi_key = os.environ.get("open_weatherApi_key")
heroku_url = os.environ.get("heroku_url")


app = Flask(__name__)

def sendmessage(chatid, text):
    URL = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
    payload = {
        "text" :text,
        "chat_id" : chatid
    }
    requests.get(URL, params=payload)


@app.route("/", methods = ["POST", "GET"])
def index():
    if(request.method == "POST"):
        resp = request.get_json()
        # print(resp)
        msgtext = resp['message']['text']
        chatid = resp['message']['chat']['id']
        if msgtext.lower() == "/start":
            sendmessage(chatid, "Hii there. Write 'HI' to get Started !!!")
        elif msgtext.lower() == 'hi' :
            sendmessage(chatid,"""Please enter the options as follows to access this tools
               
                🔥------Weather Report------🔥
    For weather report just write the city name followed by 1-
        
        ✅ example ->  1-Delhi    

            🔥------Instagram -----------🔥

    For instagram user followers count enter username followed by 2-
        
        ✅ example ->  2-shiboy_pep

            🔥 -------IMDB----------  🔥

    Enter Anything that you are familiar with, such as movie title ,album, song, etc.. followed by 3-              
       
        ✅ example -> 3-Game of Thrones   
                                """)
        else:
            if "1-" in msgtext:
                text = msgtext.split("1-")[1]
                weather(chatid, text)
                
            if "2-" in msgtext:
                text = msgtext.split("2-")[1]
                instagram(chatid, text)

                
            if "3-" in msgtext:
                text = msgtext.split("3-")[1]
                imdb(chatid, text)

    return "App is working"

@app.route("/setwebhook")
def setwebhook():
   
    url = "https://f0b7-180-151-17-204.ngrok.io" 
    s = requests.get("https://api.telegram.org/bot{}/setwebhook?url={}".format(bot_token,url))

    if s:
        return "Connection established"
    else:
        return "Connection failed"

if __name__ == "__main__":
    app.run(debug="True")