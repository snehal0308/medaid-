from flask import Flask, request , render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse,Gather
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


    if 'Hi'.lower() in msg:
        resp.message(f'Hi there! I am Mediaid bot. Please type --help to access all the commands')
    if 'help'.lower() in msg: 
        resp.message(f"COMMANDS \n '--[medicine name]: to get info on a specific medicine \n '--Issue resolved: to mark your issue as resolved'")
    if '--woods peppermint'.lower() in msg: 
        resp.message(f"This medicine is used for non productive cough \n \n Dosage: Adults and children >12 years: 2 tsps (10 mL) 3 times daily. 6-12 years: 1 tsp (5 mL) 3 times daily.\n \n Special precautions: Special precaution is needed in GI ulceration patients.Guaifenesin gives a false positive result of urinary 5-hydroxyindoleacetic acid (5-HIAA) and vanyllilmandelic acid (VMA).Use in pregnancy & lactation: Precaution is advised for pregnant and lactating mothers.' \n \n Adverse reactions might include: vomitting, dizziness, drowsiness and constipation")
    if '--nalgestan'.lower() in msg: 
        resp.message(f"This medicine is used for Nasal Decongestan \n \n Contraindications: Hyperthyroidism, HTN, coronary disease, pheochromocytoma, closed-angle glaucoma; MAOIs; lower resp tract disease. Newborn or premature infants. Lactation. \n \n Special precautions: Not recommended for anyone with kidney and liver problems \n \n Adverse reactions might include: GI disorders, difficulty in micturition, muscular weakness, tremor, hypotension, blurred vision, tinnitus, dry mouth, tightness of the chest; sweating, thirst, anorexia.")


    return str(resp)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/gather')
    gather.say('To know more about the medicine press 1') # press 2 for 2nd medicine 
    resp.append(gather)


    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)


@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('This medicine is used for non productive cough Dosage: Adults and children >12 years: 2 tsps (10 mL) 3 times daily. 6-12 years: 1 tsp (5 mL) 3 times daily. Special precautions: Special precaution is needed in GI ulceration patients.Guaifenesin gives a false positive result of urinary 5-hydroxyindoleacetic acid (5-HIAA) and vanyllilmandelic acid (VMA).Use in pregnancy & lactation: Precaution is advised for pregnant and lactating mothers. Adverse reactions might include: vomitting, dizziness, drowsiness and constipation')
            return str(resp)
        elif choice == '2':
            resp.say('his medicine is used for Nasal Decongestan. Contraindications: Hyperthyroidism, HTN, coronary disease, pheochromocytoma, closed-angle glaucoma; MAOIs; lower resp tract disease. Newborn or premature infants. Lactation. Special precautions: Not recommended for anyone with kidney and liver problems. Adverse reactions might include: GI disorders, difficulty in micturition, muscular weakness, tremor, hypotension, blurred vision, tinnitus, dry mouth, tightness of the chest; sweating, thirst, anorexia.')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/voice')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)










    
