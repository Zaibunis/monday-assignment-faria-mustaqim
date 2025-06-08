import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variable
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env file.")

# Configure the Gemini API client
genai.configure(api_key=API_KEY)

# Load the model
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Ask a question
user_input = input("Ask something: ")
response = model.generate_content(user_input)

# Print response
print("\n🤖 Gemini Response:\n", response.text)
