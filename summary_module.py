from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def summarize_text(text):
    prompt = f"""
Summarize the following educational text.

Text:
{text}

Requirements:
- Use simple English
- Keep the important points
- Make it concise
- Do not change the main meaning
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text