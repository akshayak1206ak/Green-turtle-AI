import os
import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

bcrypt = Bcrypt(app)

DATABASE = "database.db"


# ================= DATABASE INIT =================
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        user_message TEXT,
        bot_reply TEXT
    )
    """)

    conn.commit()
    conn.close()


# FORCE INIT (IMPORTANT FOR RENDER)
with app.app_context():
    init_db()


# ================= HOME =================
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("chat"))
    return redirect(url_for("login"))


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (email, password, role) VALUES (?, ?, ?)",
                (email, hashed_password, "user")
            )
            conn.commit()
        except sqlite3.IntegrityError:
            return "User already exists"
        finally:
            conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        user = cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["email"] = user[1]
            session["role"] = user[3]
            return redirect(url_for("chat"))

        return "Invalid credentials"

    return render_template("login.html")


# ================= CHAT =================
@app.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("index.html")


# ================= SAVE CHAT (OPTIONAL SIMPLE BOT) =================
@app.route("/send", methods=["POST"])
def send():
    if "user_id" not in session:
        return redirect(url_for("login"))

    message = request.form["message"]

    # simple bot reply (replace with ML later)
    reply = "You said: " + message

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chats (user_id, user_message, bot_reply)
        VALUES (?, ?, ?)
    """, (session["user_id"], message, reply))

    conn.commit()
    conn.close()

    return redirect(url_for("chat"))


# ================= HISTORY =================
@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    chats = cursor.execute("""
        SELECT user_message, bot_reply 
        FROM chats 
        WHERE user_id = ?
    """, (session["user_id"],)).fetchall()

    conn.close()

    return render_template("history.html", chats=chats)


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ================= RUN =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)