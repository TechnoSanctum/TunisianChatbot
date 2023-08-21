from flask import Flask, render_template, request
from chatterbot import ChatBot

import sys
app = Flask(__name__)
last_message = ""
rp = 0
TunisianBot = ChatBot("Tunisianbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    global last_message
    global rp
    userText = request.args.get('msg')
    if userText == "":
        return "..."
    if userText == last_message:
        rp += 1
        if rp == 3:
            return "3lah t3awed fi nafs jomla?"
        elif rp>3:
            return ''
            
        return "Najem n3awnek fi 7aja?"
    else:
        rp = 0
        last_message = userText
        return str(TunisianBot.get_response(userText))

if __name__ == "__main__":
    app.run()
