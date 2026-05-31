from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from flask_bcrypt import Bcrypt
from database import init_db

app = Flask(__name__)
app.secret_key = "supersecretkey"
bcrypt = Bcrypt(app)

init_db()


# ================= HOME =================
@app.route("/")
def home():
    return redirect(url_for("login"))


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed))
            conn.commit()
        except:
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


# ================= SMART BOT =================
def get_bot_response(message):
    message = message.lower()

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # FAQ FIRST
    cur.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + message + '%',))
    result = cur.fetchone()
    conn.close()

    if result:
        return result[0]

    # FALLBACK LOGIC
    if "hello" in message:
        return "Hi! How can I help you?"
    elif "course" in message:
        return "We offer AI, ML, Web Development courses."
    elif "fees" in message:
        return "Fees depend on course."
    elif "admission" in message:
        return "Admissions are open. Please check college portal."
    else:
        return "Admin will update my knowledge soon."


# ================= SEND MESSAGE =================
@app.route("/send_message", methods=["POST"])
def send_message():
    if "user" not in session:
        return jsonify({"error": "not logged in"}), 401

    data = request.get_json()
    msg = data["message"]
    email = session["user"]

    response = get_bot_response(msg)

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO chats (email, message, response) VALUES (?, ?, ?)",
        (email, msg, response)
    )

    conn.commit()
    conn.close()

    return jsonify({"response": response})


# ================= HISTORY =================
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


# ================= ADMIN LOGIN (SECURE FIX) =================
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM admin WHERE email=?", (email,))
        admin = cur.fetchone()
        conn.close()

        if admin and admin[2] == password:   # (OK for demo project)
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

    q = request.form["question"]
    a = request.form["answer"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO faq (question, answer) VALUES (?, ?)", (q, a))
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
        SELECT email, COUNT(*) 
        FROM chats 
        GROUP BY email 
        ORDER BY COUNT(*) DESC 
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


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)