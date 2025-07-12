import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sheshines"
    )

from flask import Flask
from flask_cors import CORS
from app.routes import main_routes

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main_routes)
    return app
