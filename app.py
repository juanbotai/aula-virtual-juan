from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "clave_secreta"

# USUARIO DE PRUEBA
usuario_db = {
    "juan": "1234"
}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    password = request.form.get("password")

    print("Usuario:", usuario)
    print("Password:", password)

    if usuario in usuario_db and usuario_db[usuario] == password:
        session["usuario"] = usuario
        return redirect("/dashboard")
    else:
        return "Credenciales incorrectas ❌"

@app.route("/dashboard")
def dashboard():
    if "usuario" in session:
        return render_template("dashboard.html", usuario=session["usuario"])
    else:
        return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))