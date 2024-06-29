import requests
import os
from fastapi import UploadFile



def photai_upscale(image_url,filename):
 
    url = 'https://prodapi.phot.ai/external/api/v2/user_activity/create-upscaler-2k'

    headers = {
        'x-api-key': os.environ.get('PHOTAI_API_KEY'),
        'Content-Type': 'application/json'
    }

    data = {
        'fileName': filename,  # Replace with the actual input file name as a string
        'sourceUrl': image_url  # Replace with the URL of your input image
    }
 
    response = requests.post(url, headers=headers, json=data)
 
    if response.status_code == 200:
        return response.json()['data']['2k']['url']
    else:
        return f"Error: {response.status_code} - {response.text}"


def limewire_upscale(image: UploadFile):
    image_contents = image.file.read()

    url = "https://api.limewire.com/api/image/upscaling"

    payload = {
        "image": image_contents,
        "upscale_factor": 2
    }

    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('LIMEWIRE_API_KEY')}"
    }


    with open(image, 'rb') as image_file:
        image_contents = image_file.read()
        response = requests.post(url, headers=headers, files={'image': image_file})

        data = response.json()

    return data
