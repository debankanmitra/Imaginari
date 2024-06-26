import requests
from pydantic import BaseModel
from typing import Optional
import os

class Item(BaseModel):
    style: Optional[str] = None
    prompt: str
    negative_prompt: Optional[str] = None

def limewire(style, prompt, negative_prompt):

    url = "https://api.limewire.com/api/image/generation"

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "samples": 1,
        "aspect_ratio": "1:1",
        "style": style
    }

    token = 'lmwr_sk_EMgUw3WKFf_KPjr24wAjxj0jI6ha9R3i7jsbzZGbXvHl9ipE'

    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    # credits_remaining=response.json()['credits_remaining']
    url = response.json()['data'][0]['asset_url']

    return {"url": url}
