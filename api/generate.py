import requests
from pydantic import BaseModel
from typing import Optional
import os

class Item(BaseModel):
    style: Optional[str] = None
    prompt: str
    negative_prompt: Optional[str] = None

def limewire(style, prompt, negative_prompt):
    if not style or not prompt:
        raise ValueError("Style and prompt must be provided")

    url = "https://api.limewire.com/api/image/generation"

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "samples": 1,
        "aspect_ratio": "1:1",
        "style": style
    }

    token = os.environ.get('LIMEWIRE_API_KEY')

    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    credits_remaining=response.json()['credits_remaining']
    url = response.json()
    print(url)

    return {"credits_remaining": credits_remaining, "url": url}
