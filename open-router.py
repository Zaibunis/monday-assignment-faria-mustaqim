import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "https://yourapp.com",
    "X-Title": "Test App"
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello!"}]
    }
)

print(response.json())
