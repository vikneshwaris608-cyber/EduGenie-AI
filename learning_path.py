from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_learning_path(topic):
    prompt = f"""
Create a personalized learning path for:

Topic:
{topic}

Structure the learning path from beginner to advanced.

Include:
- Beginner topics
- Intermediate topics
- Advanced topics
- Suggested learning order
- Simple practice suggestions

Use simple English and clear formatting.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
