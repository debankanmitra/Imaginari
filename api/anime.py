from fastapi import UploadFile
import replicate
import requests
from typing import Dict
import os

def dreamshaperXL(image, prompt, negative_prompt):
    input = {
        "image": image,
        "prompt": prompt,
        "negative_prompt": negative_prompt
    }

    api = replicate.Client(api_token=os.environ.get('REPLICATE_API_TOKEN'))

    output = api.run(
        "grandlineai/instant-id-artistic:0343e59373a43df5a2e9ce96d11c1259108a7660ae4d4a6ef9340014d7b14ed9",
        input=input
    )

    return output

def face2paint(image: UploadFile):
    URL = "https://phototoanime1.p.rapidapi.com/photo-to-anime"

    # Read the contents of the image file as bytes
    image_bytes = image.file.read()

    # Open the image file and read its content as bytes
    files = {"image": image_bytes}

    payload = {
        "style": "face2paint"  # Removed the "url" field since we're using a local file
    }

    headers = {
        "X-RapidAPI-Key": os.environ.get('RAPIDAPI_TOKEN'), # 0717583e3emsh87521118c5fdb03p115662jsne0ab48a9cea6
        "X-RapidAPI-Host": "phototoanime1.p.rapidapi.com"
    }

    response = requests.post(URL, data=payload, files=files, headers=headers)

    return response.json()


# replicate model : https://replicate.com/grandlineai/instant-id-artistic