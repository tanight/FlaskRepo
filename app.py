from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
 
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
 
    resp = MessagingResponse()
    resp.message('SUCK MY ASS')
    return str(resp)
 
if __name__ == '__main__':
    app.run()
