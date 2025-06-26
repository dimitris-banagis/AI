import openai
import os
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    img_data = requests.get(image_url).content
    img = Image.open(BytesIO(img_data))
    img.show()
    img.save("generated_image.png")

if __name__ == "__main__":
    user_prompt = input("Περιγραφή εικόνας: ")
    generate_image(user_prompt)
