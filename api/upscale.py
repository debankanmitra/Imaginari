import requests




def photai_upscale(image_url,filename):
 
    url = 'https://prodapi.phot.ai/external/api/v2/user_activity/create-upscaler-2k'

    headers = {
        'x-api-key': '6624c8ef4f19180796bc9040_e1900e9cdb9973724f61_apyhitools',
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
 