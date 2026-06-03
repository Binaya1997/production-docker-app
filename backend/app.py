from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

@app.route("/")
def home():
    return "Backend API Running"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")

        version = cur.fetchone()

        cur.close()
        conn.close()

        return f"PostgreSQL Connected: {version}"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
