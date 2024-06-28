# DOCS: https://docs.phot.ai/advanced/Old_photos_restoration

import cloudinary.uploader
import requests
from fastapi import UploadFile
import cloudinary
import replicate
import os


def cloudinary_upload(image: UploadFile):
    cloudinary.config( 
        cloud_name = "dv0zkyn0a", 
        api_key = '129753673536953', 
        api_secret = 'kwPv2OaL9blJmeh3Z50SCF9Uv1c' 
    )

    image_contents = image.file.read()
    res=cloudinary.uploader.upload(image_contents, folder="",resource_type="image")
    name = res["public_id"]+"."+res["format"]
    url=res["url"]
    resout = {"url":url,"name":name}
    return resout



def restoreimg(cloudinary_url,filename):

    url = 'https://prodapi.phot.ai/external/api/v2/user_activity/old-photos-restore-2k'

    headers = {
    'x-api-key': '667e72e2ec4620bebeef983c_5a94918ad1982dec4ddf_apyhitools',
    'Content-Type': 'application/json'
    }

    data = {
    'fileName': filename,  # Replace with the actual input file name as a string
    'input_image_link': cloudinary_url,  # Replace with the URL of your input image
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

# REPLICATE : 
# https://replicate.com/microsoft/bringing-old-photos-back-to-life/versions/c75db81db6cbd809d93cc3b7e7a088a351a3349c9fa02b6d393e35e0d51ba799


def microsoft_restore(cloudinary_url):
    api = replicate.Client(api_token=os.environ.get('REPLICATE_API_TOKEN'))

    input = {
        "image": cloudinary_url
    }

    output = api.run(
        "microsoft/bringing-old-photos-back-to-life:c75db81db6cbd809d93cc3b7e7a088a351a3349c9fa02b6d393e35e0d51ba799",
        input=input
    )

    return output
