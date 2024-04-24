from fastapi import FastAPI, File, UploadFile, Form
from api.anime import dreamshaperXL,face2paint
from api.restore import restoreimg,cloudinary_upload
from api.removebg import Background_Removal
from api.generate import limewire,Item
from api.outpaint import segmindOutpaint




app = FastAPI()

@app.post("/generate")
def generate(item: Item):
    response = limewire(item.style, item.prompt, item.negative_prompt)
    return {"output": response['url']}

@app.get("/edit")
async def edit():
    return {"message": "Hello World2"}

@app.get("/upscale")
async def upscale():
    return {"message": "Hello World3"}

@app.get("/Inpainting")
async def inpainting():
    return {"message": "Hello World4"}

@app.post("/outpainting")
def outpainting(image: UploadFile = File(...),prompt: str = Form(...),negative_prompt: str = Form(None)):
    file = cloudinary_upload(image)
    response = segmindOutpaint(file['url'], prompt, negative_prompt)
    return {"output": response}

@app.post("/removebg")
def removebg(image: UploadFile = File(...)):
    file = cloudinary_upload(image)
    response = Background_Removal(file['url'])
    return {"output": response}

@app.post("/restore")
def restore(image: UploadFile = File(...)):
    imgfile = cloudinary_upload(image)
    response = restoreimg(imgfile['url'],imgfile['name'])
    return {"output": response['data']['2k']['url']}

@app.post("/toanime")
def toanime(image: UploadFile = File(...)):
    response_url = face2paint(image)
    return {"output": response_url['body']['imageUrl']}