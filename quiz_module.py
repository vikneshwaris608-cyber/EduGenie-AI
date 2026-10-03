from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_quiz(topic):
    prompt = f"""
Create a quiz about the following educational topic:

Topic:
{topic}

Create exactly 3 multiple-choice questions.

For each question provide:
- question
- exactly 4 options
- answer as the correct option number (0, 1, 2, or 3)

Return ONLY valid JSON in this format:

[
    {{
        "question": "Question here",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "answer": 0
    }}
]
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)