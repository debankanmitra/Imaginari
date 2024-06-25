from io import BytesIO
import cloudinary.uploader
import requests
import cloudinary
import os

def Background_Removal(imageUrl):
      cloudinary.config( 
        cloud_name = "dv0zkyn0a", 
        api_key = os.environ.get('CLOUDINARY_API_KEY'), 
        api_secret = os.environ.get('CLOUDINARY_API_SECRET') 
    )

      url = "https://api.segmind.com/v1/bg-removal"
      headers = {"x-api-key": os.environ.get('SEGMIND_API_KEY')}

      data = {"method": "object", "imageUrl": imageUrl}
      response = requests.post(url, json=data, headers=headers)
      if response.status_code == 200:
          image=BytesIO(response.content)
          res=cloudinary.uploader.upload(image, folder="",resource_type="image")
          return res['url']
      else:
          raise Exception(f"Error: {response.status_code}")