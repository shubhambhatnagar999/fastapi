from database import db
from bson import ObjectId
from fastapi import Query, HTTPException, UploadFile, File
import os, shutil, uuid

# Ensure uploads folder exists
UPLOAD_FOLDER = "uploads/sliders"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_all_sliders():
    sliders = list(db['sliders'].find({}))
    for slider in sliders:
        slider["_id"] = str(slider["_id"])
    return sliders

def create_sliders(slider_data):
    file = slider_data["image_path"]
    title = slider_data["title"]
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image")

    file_path = os.path.join(UPLOAD_FOLDER,  f"{uuid.uuid4()}_{file.filename}")

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    slider_data = {
        "title": title,
        "image_path": file_path
    }

    # Call service
    result = db['sliders'].insert_one(slider_data)

    return {"filename": file.filename, "message": "Image uploaded successfully"}

def delete_slider(slider_id: str):
    result = db['sliders'].delete_one({"_id": ObjectId(slider_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Slider not found")
    return {"message": "Slider deleted successfully"}

def get_slider_by_id(slider_id: str):
    try:
        obj_id = ObjectId(slider_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid slider ID")

    slider = db['sliders'].find_one({"_id": obj_id})
    if not slider:
        raise HTTPException(status_code=404, detail="Slider not found")
    slider["_id"] = str(slider["_id"])
    return slider