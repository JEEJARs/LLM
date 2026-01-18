import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
ช่วยคิดชื่อร้านดอกไม้ให้หน่อย โดยให้ชื่อร้านที่ขาย ช่อดอกไม้ และ ดอกไม้แห้ง มากกว่าดอกไม้สด
"""

response = client.models.generate_content(
  model='gemini-2.5-flash-lite',
  contents=prompt
)

print("\nResponse:")
print(response.text)