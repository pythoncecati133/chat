from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

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
