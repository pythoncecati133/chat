from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = 'ACb700a1f67a45ade388c61ab553c29182'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+5219671584449'
)

print(message.sid)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtén el mensaje recibido
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    reply = response.message()
    
    # Respuestas automáticas
    if 'hola' in incoming_msg:
        reply.body('¡Hola! ¿En qué puedo ayudarte?')
    elif 'precio' in incoming_msg:
        reply.body('Nuestros precios son los más competitivos del mercado.')
    else:
        reply.body('Lo siento, no entiendo tu mensaje.')

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
