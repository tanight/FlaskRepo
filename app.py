from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from twilio.rest import Client
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
 
    resp = MessagingResponse()
    resp.message('Thank you for informing us on the changes for {}, we\'ll start updating our databases to show current street parking avalibility. '.format( message_body))
    return str(resp)
 


account_sid = "AC5ccfa100339e3935f8159448cb57e50f"
auth_token = "4422619d51ea241335647acac2e2ce84"
client = Client(account_sid, auth_token)

call = client.api.account.calls\
      .create(to="+9172888938",  # Any phone number
              from_="+12012926798 ", # Must be a valid Twilio number
              url="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiJhIPFwfLWAhXHNiYKHeZFAtcQ3ywIKjAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dw5Fgp-KihIA&usg=AOvVaw1KIJFh7k8enVSUIOzhYgTh")

print(call.sid)

if __name__ == '__main__':
    app.run()