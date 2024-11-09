import os
from openai import OpenAI
import base64
import json

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# image_path = "Pictures/IMG_2316.jpg"

# base64_image = encode_image(image_path)
# # print(base64_image)
# with open("base64.txt", "w") as f:
#     f.write(base64_image)
#     f.close()

def extract_details(base64_image):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "can you extract machine information from this image? return a json object and translate whichever language to english. just return a json object alone and no text other than that. i want equipment name, manufacturer, model, serial number, equipment type(eg. structural, ventilation etc), size, age, type of material. if you are not sure then just put None. you can also add any extra machine information you can extract as a seperate dictionary in the output under 'additional data'. do not return anything other than a json object."},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "high"
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    return (json.loads(response.choices[0].message.content[8:].rstrip('`')))

