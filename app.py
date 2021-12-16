from flask import Flask,request
import requests
import sys
from credentials import bot_token,openweather_api_key
from features import weatherReport, instagram

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
            sendmessage(chatid,"""Please enter the options as follows
                                 For weather report just write the city name
                                 ------Instagram ------ 
                                 Please enter the username 
                                 """)
            return "OK"
           
        if msgtext.lower()=='weather' :
            sendmessage(chatid,"""Please enter the city name as follows
                                 Hyderabad   """)
            return "OK"
           
        # weatherReport(chatid, msgtext)
        instagram(chatid,msgtext)
    
       
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
