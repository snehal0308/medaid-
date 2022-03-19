from flask import Flask, request , render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from os import path



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()


    if '--Tasks'.lower() in msg:
        resp.message(f'Hello!')



    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)