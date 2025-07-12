import requests

HF_API_KEY = ""
API_URL = ""
headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

prompt = "Suggest 3 startup ideas for women in fashion designing."

response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

print(f"Status code: {response.status_code}")
try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Failed to parse JSON:", e)
    print("Response text:", response.text)
