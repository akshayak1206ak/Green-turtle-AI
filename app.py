from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask_bcrypt import Bcrypt
from database import init_db

app = Flask(__name__)
app.secret_key = "supersecretkey"
bcrypt = Bcrypt(app)

init_db()
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                           (email, hashed_password))
            conn.commit()
        except:
            return "User already exists!"

        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            session["user"] = email
            return redirect(url_for("chat"))
        else:
            return "Invalid credentials"

    return render_template("login.html")
@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("index.html", user=session["user"])@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))