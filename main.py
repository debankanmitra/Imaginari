from fastapi import FastAPI, File, UploadFile, Form
from api.anime import face2paint
from api.restore import restoreimg,cloudinary_upload
from api.removebg import Background_Removal
from api.generate import limewire,Item
from api.outpaint import segmindOutpaint
from api.upscale import photai_upscale
from api.inpaint import segmindInpaint
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mangum import Mangum

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5173",
    "https://imaginari-one.vercel.app",
    "https://imaginari-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app, lifespan="off")

@app.get("/test")
def test():
    return {"message": "Hello World"}

@app.post("/generate")
def generate(item: Item):
    response = limewire(item.style, item.prompt, item.negative_prompt)
    return {"output": response['url']}


@app.post("/upscale")
def upscale(image: UploadFile = File(...)):
    file = cloudinary_upload(image)
    response = photai_upscale(file['url'],file['name'])
    return {"output": response}

@app.post("/inpainting")
def inpainting(image: UploadFile = File(...),mask: UploadFile = File(...),prompt: str = Form(...),negative_prompt: str = Form(None)):
    image = cloudinary_upload(image)
    mask = cloudinary_upload(mask)
    response = segmindInpaint(image['url'],mask['url'],prompt,negative_prompt)
    return {"output": response}

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



if __name__ == "__main__":
    uvicorn.run(app)