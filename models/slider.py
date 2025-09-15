from pydantic import BaseModel
from fastapi import UploadFile, File, Form
class SliderCreate(BaseModel):
    title: str = Form(...),
    image: UploadFile = File(...)