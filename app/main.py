from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.openai_client import generate_image

app = FastAPI()

class TextRequest(BaseModel):
    prompt: str

@app.post("/generate-image")
async def create_image(request: TextRequest):
    try:
        image_url = generate_image(request.prompt)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
