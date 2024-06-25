import requests
import os



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
 