import os
from dotenv import load_dotenv

load_dotenv()

# Ensure the API key is set correctly from the environment variable


import openai

openai.api_key = os.getenv("OPENAI_API")

# client = OpenAI()

# Example usage of the OpenAI API to generate a text completion
try:
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": "Hello, world!"}
        ]
    )
    print(response)
except Exception as e:
    print("An error occurred:", e)
