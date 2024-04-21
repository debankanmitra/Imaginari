from fastapi import FastAPI,UploadFile, File
from api.anime import dreamshaperXL,face2paint
from api.restore import restoreimg,cloudinary_upload



app = FastAPI()

@app.get("/generate")
async def generate():
    return {"message": "Hello World"}

@app.get("/edit")
async def edit():
    return {"message": "Hello World2"}

@app.get("/upscale")
async def upscale():
    return {"message": "Hello World3"}

@app.get("/Inpainting")
async def inpainting():
    return {"message": "Hello World4"}

@app.get("/outpainting")
async def outpainting():
    return {"message": "Hello World5"}

@app.get("/removebg")
async def removebg():
    return {"message": "Hello World6"}

@app.post("/restore")
def restore(image: UploadFile = File(...)):
    imgfile = cloudinary_upload(image)
    response = restoreimg(imgfile['url'],imgfile['name'])
    return {"output": response['data']['2k']['url']}

@app.post("/toanime")
def toanime(image: UploadFile = File(...)):
    response_url = face2paint(image)
    return {"output": response_url['body']['imageUrl']}