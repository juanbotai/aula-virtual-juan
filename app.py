<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("login.html")

app.run(debug=True)
=======
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
>>>>>>> b1d3ec79d31bfbc8cabf105f911d29b2add333e5
