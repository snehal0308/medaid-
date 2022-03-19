from flask import Flask, request , render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from os import path



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/sms", methods=['POST'])
def sms_reply():

    msg = request.form.get('Body').lower()
    resp = MessagingResponse()


    if msg == 'hello': 
        resp.message('hi!')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
