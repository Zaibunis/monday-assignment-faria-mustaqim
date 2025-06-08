import os
from dotenv import load_dotenv
import litellm

# Load your OpenRouter API key from .env
load_dotenv()

# Optional: Enable debugging (if needed)
# litellm._turn_on_debug()

# Ask user for input
user_question = input("Ask a question: ")

# Get completion from OpenRouter model
response = litellm.completion(
    model="openai/gpt-3.5-turbo",  # Change to any OpenRouter-supported model
    messages=[{"role": "user", "content": user_question}],
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://openrouter.ai/api/v1"
)

# Print the assistant's reply
print("\nAnswer:")
print(response['choices'][0]['message']['content'])
