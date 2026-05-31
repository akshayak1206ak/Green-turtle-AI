import os
from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # change this for security
bcrypt = Bcrypt(app)

DATABASE = "database.db"


# ---------------- DATABASE CONNECTION ----------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- HOME ----------------
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("chat"))
    return redirect(url_for("login"))


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (email, password, role) VALUES (?, ?, ?)",
            (email, hashed_password, "user")
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cursor = conn.cursor()

        user = cursor.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()

        conn.close()

        if user and bcrypt.check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["email"] = user["email"]
            session["role"] = user["role"]

            return redirect(url_for("chat"))

        return "Invalid login credentials"

    return render_template("login.html")


# ---------------- CHAT PAGE ----------------
@app.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("index.html")


# ---------------- CHAT HISTORY ----------------
@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cursor = conn.cursor()

    chats = cursor.execute(
        "SELECT user_message, bot_reply FROM chats WHERE user_id = ?",
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template("history.html", chats=chats)


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)