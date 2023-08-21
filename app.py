from flask import Flask, render_template, request

app = Flask(__name__)
'''
last_message = ""
rp = 0
TunisianBot = ChatBot("Tunisianbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
'''

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    
    userText = request.args.get('msg')
    return userText
if __name__ == "__main__":
    app.run()
