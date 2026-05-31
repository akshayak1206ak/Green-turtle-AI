import sqlite3
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

email = "admin@gmail.com"
password = "admin123"

hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

cursor.execute("""
INSERT OR IGNORE INTO users (email, password, role)
VALUES (?, ?, ?)
""", (email, hashed_password, "admin"))

conn.commit()
conn.close()

print("Admin created successfully")
