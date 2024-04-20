from fastapi import FastAPI,UploadFile, File
from api.anime import dreamshaperXL,face2paint



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

@app.get("/restore")
async def restore():
    return {"message": "Hello World7"}

@app.post("/toanime")
def toanime(image: UploadFile = File(...)):
    response_url = face2paint(image)
    return {"output": response_url['body']['imageUrl']}