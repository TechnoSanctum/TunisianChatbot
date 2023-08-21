from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

if __name__ == "__main__":
    app.run()
