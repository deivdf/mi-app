from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "10.0.2.X"),  # IP privada EC2-DB
        user=os.getenv("DB_USER", "app_user"),
        password=os.getenv("DB_PASS", ""),
        database=os.getenv("DB_NAME", "app_db")
    )

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Flask en EC2 🚀"})

@app.route("/datos")
def datos():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM registros LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
