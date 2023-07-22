from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/test-upload")
async def test_upload(image: UploadFile = File(...)):
    return {"filename": image.filename}
 