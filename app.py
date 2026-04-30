from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="devops"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100)
)
""")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        cursor.execute("INSERT INTO users(name) VALUES(%s)", (name,))
        db.commit()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template("index.html", users=data)

@app.route("/health")
def health():
    return "OK", 200

app.run(host="0.0.0.0", port=5000)
