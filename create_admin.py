import sqlite3
from flask_bcrypt import Bcrypt

def create_admin(email, password):
    bcrypt = Bcrypt()

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO admin (email, password)
    VALUES (?, ?)
    """, (email, hashed_password))

    conn.commit()
    conn.close()

    print("Admin created successfully")

if __name__ == "__main__":
    create_admin("admin@gmail.com", "admin123")