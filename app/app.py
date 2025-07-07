from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            dbname=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD']
        )
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
