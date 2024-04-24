from io import BytesIO
import cloudinary.uploader
import requests
import cloudinary

def Background_Removal(imageUrl):
      cloudinary.config( 
        cloud_name = "dv0zkyn0a", 
        api_key = "129753673536953", 
        api_secret = "kwPv2OaL9blJmeh3Z50SCF9Uv1c" 
    )

      url = "https://api.segmind.com/v1/bg-removal"
      headers = {"x-api-key": "SG_ea36d835d551d052"}

      data = {"method": "object", "imageUrl": imageUrl}
      response = requests.post(url, json=data, headers=headers)
      if response.status_code == 200:
          image=BytesIO(response.content)
          res=cloudinary.uploader.upload(image, folder="",resource_type="image")
          return res['url']
      else:
          raise Exception(f"Error: {response.status_code}")