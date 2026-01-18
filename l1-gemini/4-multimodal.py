import os
from google import genai
from PIL import Image

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

image = Image.open("banded_krait.jpeg")
image.thumbnail([512,512])

image1 = Image.open("bluering.png")
image1.thumbnail([512,512])

image2 = Image.open("frog dart.jpeg")
image2.thumbnail([512,512])


response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=[
        image,image1,image2,
        "เขียนคำอธิบายสั้นๆ ของภาพนี้ ซึ่งเหมาะสำหรับเป็นสารคดีสัตว์ป่าเพื่อการศึกษาสำหรับเด็กอายุต่ำกว่า 10 ปี รวมถึงชื่อของสัตว์ ถิ่นที่อยู่อาศัย และข้อเท็จจริงสนุกๆ เกี่ยวกับสัตว์นั้นๆ และบอกด้วยว่าสัตว์ตัวไหนอันตรายกว่ากัน"
    ]
)
print("\nResponse:")
print(response.text)