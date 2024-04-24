import requests
from pydantic import BaseModel
from typing import Optional

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

    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": "Bearer lmwr_sk_qVretommpl_vw8PBAgja0oO8SG20NlR0eIFQa4xGDng71utP"
    }

    response = requests.post(url, json=payload, headers=headers)
    credits_remaining=response.json()['credits_remaining']
    url = response.json()['data'][0]['asset_url']

    return {"credits_remaining": credits_remaining, "url": url}
