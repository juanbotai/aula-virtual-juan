from flask import request
from twilio.twiml.messaging_response import MessagingResponse

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.values.get('Body', '').lower()
    
    resp = MessagingResponse()
    reply = resp.message()

    reply.body("Hola Juan, tu bot ya funciona 🚀")

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
