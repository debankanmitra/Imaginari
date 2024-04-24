import requests
import cloudinary
from io import BytesIO
import cloudinary.uploader
from base64 import b64encode

def toB64(imgUrl):
    return str(b64encode(requests.get(imgUrl).content))[2:-1]

def segmindOutpaint(imageUrl,prompt,negative_prompt):
    prmpt = str(prompt)
    negprmpt = str(negative_prompt)
    cloudinary.config( 
        cloud_name = "dv0zkyn0a", 
        api_key = "129753673536953", 
        api_secret = "kwPv2OaL9blJmeh3Z50SCF9Uv1c" 
    )
    url = "https://api.segmind.com/v1/sd1.5-outpaint"

    # Request payload
    data = {
  "image": toB64(imageUrl),
  "prompt": prmpt,
  "negative_prompt": negprmpt,
  "scheduler": "DDIM",
  "num_inference_steps": 25,
  "img_width": 1024,
  "img_height": 1024,
  "scale": 1,
  "strength": 1,
  "offset_x": 256,
  "offset_y": 256,
  "guidance_scale": 7.5,
  "mask_expand": 8,
  "seed": 124567
    }

    response = requests.post(url, json=data, headers={'x-api-key': "SG_ea36d835d551d052"})

    if response.status_code == 200:
          image=BytesIO(response.content)
          res=cloudinary.uploader.upload(image, folder="",resource_type="image")
          return res['url']
    else:
        raise Exception(f"Error: {response.status_code}")