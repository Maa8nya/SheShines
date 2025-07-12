from flask import Blueprint, request, jsonify , render_template
from app.db import get_db_connection
from flask import app

main_routes = Blueprint('main', __name__)

@main_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({"message": "Missing required fields!"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        return jsonify({"message": "Email already exists!"}), 400

    cursor.execute("""
    INSERT INTO users (name, email, password)
    VALUES (%s, %s, %s)
""", (name, email, password))

    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Profile created successfully!"}), 201


# startup ideas feature !!!!

from flask import Blueprint, request, jsonify, render_template
import requests

HF_API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def query_huggingface(prompt):
    print(f"Querying HuggingFace with prompt: {prompt}")
    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "options": {"wait_for_model": True}
    })
    print(f"Status code: {response.status_code}")
    try:
        response_json = response.json()
        print("Response JSON:", response_json)
    except Exception as e:
        print("Failed to parse JSON response:", e)
        print("Response text:", response.text)

    if response.status_code == 200:
        if isinstance(response_json, list) and 'generated_text' in response_json[0]:
            generated_text = response_json[0]['generated_text']
            print(f"Generated text: {generated_text}")
            return generated_text.strip()
        else:
            print("Unexpected response format.")
            return "Sorry, couldn't generate a response right now."
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Sorry, couldn't generate a response right now."

@main_routes.route('/')
def home():
    return render_template('chatbot.html')

@main_routes.route('/get_ideas', methods=['POST'])
def get_ideas():
    data = request.get_json()
    field = data.get('field')
    print(f"Received field: {field}")
    prompt = f"Give me 3 startup ideas for women in the field of {field}."
    result = query_huggingface(prompt)
    print(f"Returning result: {result}")
    return jsonify({"ideas": [result]})

if __name__ == "__main__":
    app.run(debug=True)
