from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def answer_question(question):
    prompt = f"""
Answer the following educational question clearly and accurately.

Question:
{question}

Requirements:
- Use simple English
- Give a direct answer
- Explain briefly when necessary
- Avoid unnecessary information
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text