import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """
Hello! You are an AI chatbot for a travel web site.
Your mission is to provide helpful queries for travelers.
Remember that before you answer a question, you must check to see if it complies with your mission.
If not, you can say, "Sorry I can't answer that question."
"""
prompt = "How do I make pizza dough at home?"

response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print(response.text)