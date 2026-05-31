import os
import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
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
        role TEXT DEFAULT 'user'
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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faq (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()


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

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, hashed)
            )
            conn.commit()
        except:
            return "User already exists"
        finally:
            conn.close()

        return redirect("/login")

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
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["email"] = user[1]
            session["role"] = user[3]
            return redirect("/chat")

        return "Invalid credentials"

    return render_template("login.html")


# ================= CHAT PAGE =================
@app.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect("/login")

    return render_template("index.html", user=session["email"])


# ================= FIXED SEND MESSAGE API =================
@app.route("/send_message", methods=["POST"])
def send_message():
    if "user_id" not in session:
        return jsonify({"error": "not logged in"})

    data = request.get_json()
    message = data.get("message")

    reply = "You said: " + message

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chats (user_id, user_message, bot_reply)
        VALUES (?, ?, ?)
    """, (session["user_id"], message, reply))

    conn.commit()
    conn.close()

    return jsonify({"response": reply})


# ================= HISTORY =================
@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    chats = cursor.execute("""
        SELECT user_message, bot_reply 
        FROM chats 
        WHERE user_id=?
    """, (session["user_id"],)).fetchall()

    conn.close()

    return render_template("history.html", chats=chats)


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ================= ADMIN (FIXED ROUTES) =================
@app.route("/admin")
def admin():
    return render_template("admin.html", users=[], chats=[])


@app.route("/analytics")
def analytics():
    return render_template(
        "analytics.html",
        users_count=0,
        chats_count=0,
        top_users=[]
    )


@app.route("/add_faq", methods=["POST"])
def add_faq():
    question = request.form["question"]
    answer = request.form["answer"]

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")


# ================= RUN =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)