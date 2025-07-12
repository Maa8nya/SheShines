# app/models.py

import mysql.connector
from flask import current_app

def get_db_connection():
    conn = mysql.connector.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['ROOT'],
        password=current_app.config['ROOT'],
        database=current_app.config['SHESHINES']
    )
    return conn

def create_profile(name, email, phone_number, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO profiles (name, email, phone_number, password)
        VALUES (%s, %s, %s, %s)
    """, (name, email, phone_number, password))
    conn.commit()
    cursor.close()
    conn.close()
