import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

print(f"Testing API Key: {api_key[:10]}...")

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    # "HTTP-Referer": "http://localhost:8501", # Optional
    # "X-Title": "Career GPS", # Optional
}
data = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [{"role": "user", "content": "Hello!"}],
}

try:
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
