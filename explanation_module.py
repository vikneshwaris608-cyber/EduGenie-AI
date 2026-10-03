from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_concept(topic):
    prompt = f"""
Explain the following topic in simple language for a beginner.

Topic: {topic}

Requirements:
- Use simple English
- Keep the explanation easy to understand
- Give a clear explanation
- Include a simple example if useful
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text