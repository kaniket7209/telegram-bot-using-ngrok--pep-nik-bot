from flask import Flask,request
import requests
import sys
from credentials import bot_token,openweather_api_key
from features import weatherReport, instagram, imdb

key = bot_token
app = Flask(__name__)

def sendmessage(chatid, text):
    URL = "https://api.telegram.org/bot{}/sendMessage".format(key)
    payload = {
        "text":text,
        "chat_id":chatid
        }
    resp = requests.post(URL,params = payload)



@app.route("/",methods=["POST","GET"])
def index():
    if(request.method == "POST"):
       
        resp = request.get_json()
        # print(resp)
        msgtext = resp["message"]["text"]
        chatid = resp["message"]["chat"]["id"]
        sendmessage(chatid, msgtext)
        if msgtext.lower() == '/start':
            sendmessage(chatid,"Hi there start by typing 'hi' ")
            return "OK"
        if msgtext.lower()=='hi' :
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
            return "OK"
        
        if "1-" in msgtext:
            text = msgtext.split("1-")[1]
            weatherReport(chatid, text)

        if "2-" in msgtext:
            text = msgtext.split("2-")[1]
            instagram(chatid,text)

        if "3-" in msgtext:
            text = msgtext.split("3-")[1]
            imdb(chatid, text)
    
       
    return "Done"

@app.route("/setwebhook/")
def setwebhook():
    url = "https://b67e-180-151-17-204.ngrok.io/"
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(key,url))
    if s:
        return "yes"
    else:
        return "fail"

if __name__ == "__main__":
    app.run(debug=True)
