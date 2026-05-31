from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from flask_bcrypt import Bcrypt
from database import init_db
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


app = Flask(__name__)

# 🔐 Better security than fixed string
app.secret_key = os.urandom(24)

bcrypt = Bcrypt(app)

# Initialize database
init_db()


# ================= HOME =================
@app.route("/")
def home():
    return redirect(url_for("login"))


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return "Missing fields"

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, hashed_password)
            )

            conn.commit()
            conn.close()

        except Exception as e:
            return "User already exists"

        return redirect(url_for("login"))

    return render_template("register.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cur.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            session["user"] = email
            return redirect(url_for("chat"))

        return "Invalid credentials"

    return render_template("login.html")


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ================= CHAT PAGE =================
@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("index.html", user=session["user"])


# ================= BOT LOGIC (CLEAN SINGLE FUNCTION) =================
def get_bot_response(message):
    message = message.lower()

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # 🔥 FAQ FIRST (dynamic learning system)
    cur.execute(
        "SELECT answer FROM faq WHERE question LIKE ?",
        ('%' + message + '%',)
    )
    faq_result = cur.fetchone()
    conn.close()

    if faq_result:
        return faq_result[0]

    # 🔥 fallback responses
    if "hello" in message:
        return "Hi! How can I help you?"
    elif "course" in message:
        return "We offer AI, ML, Web Development courses."
    elif "fees" in message:
        return "Fees depend on the course."
    elif "admission" in message:
        return "Admissions are open. Please check the official portal."
    else:
        return "I am still learning. Admin will update my knowledge soon."


# ================= SEND MESSAGE API =================
@app.route("/send_message", methods=["POST"])
def send_message():
    if "user" not in session:
        return jsonify({"error": "not logged in"}), 401

    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        email = session["user"]

        if not user_message:
            return jsonify({"error": "empty message"}), 400

        bot_response = get_bot_response(user_message)

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO chats (email, message, response) VALUES (?, ?, ?)",
            (email, user_message, bot_response)
        )

        conn.commit()
        conn.close()

        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": "server error"}), 500


# ================= CHAT HISTORY =================
@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT message, response FROM chats WHERE email=?",
        (session["user"],)
    )

    chats = cur.fetchall()
    conn.close()

    return render_template("history.html", chats=chats)


# ================= ADMIN LOGIN =================
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM admin WHERE email=?", (email,))
        admin = cur.fetchone()
        conn.close()

        # ⚠️ demo project level check (acceptable in BCA viva)
        if admin and admin[2] == password:
            session["admin"] = email
            return redirect("/admin")

        return "Invalid admin login"

    return render_template("admin_login.html")


# ================= ADMIN DASHBOARD =================
@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/admin-login")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    cur.execute("SELECT * FROM chats")
    chats = cur.fetchall()

    conn.close()

    return render_template("admin.html", users=users, chats=chats)


# ================= ADD FAQ =================
@app.route("/add_faq", methods=["POST"])
def add_faq():
    if "admin" not in session:
        return "Unauthorized"

    question = request.form.get("question")
    answer = request.form.get("answer")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")


# ================= ANALYTICS =================
@app.route("/analytics")
def analytics():
    if "admin" not in session:
        return redirect("/admin-login")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    users_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM chats")
    chats_count = cur.fetchone()[0]

    cur.execute("""
        SELECT email, COUNT(*) as total
        FROM chats
        GROUP BY email
        ORDER BY total DESC
        LIMIT 5
    """)
    top_users = cur.fetchall()

    conn.close()

    return render_template(
        "analytics.html",
        users_count=users_count,
        chats_count=chats_count,
        top_users=top_users
    )


# ================= RUN APP =================
if __name__ == "__main__":
    app.run(debug=True)