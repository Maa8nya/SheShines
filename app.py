from flask import Flask, render_template
from flask_cors import CORS
from app.routes import main_routes, query_huggingface
import sqlite3

app = Flask(__name__)
CORS(app)

app.register_blueprint(main_routes)

# Function to fetch user data from the database
def get_user_profile(user_id):
    conn = sqlite3.connect('Experts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, phone_number, password FROM users WHERE id = ?", (user_id,))
    data = cursor.fetchone()
    conn.close()
    return data

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user_data = get_user_profile(user_id)
    if user_data:
        return render_template('profilepage.html',
                               name=user_data[0],
                               email=user_data[1],
                               phone_number=user_data[2],
                               password=user_data[3])
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)

#startup ideas feature!!!!

from flask import Flask, render_template, request, jsonify
from ideas_data import startup_ideas
import random

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')  # Explicitly set folder

@app.route('/')
def home():
    return render_template('chatbot.html')  # your chatbot interface

@app.route('/get_ideas', methods=['POST'])
def get_ideas():
    data = request.get_json()
    field = data.get('field')
    prompt = f"Give me 3 startup ideas for women in the field of {field}."
    print(f"Received prompt: {prompt}")
    idea_text = query_huggingface(prompt)
    print(f"Sending ideas to frontend: {idea_text}")
    ideas = [line.strip() for line in idea_text.split('\n') if line.strip()]
    return jsonify({"ideas": ideas})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

