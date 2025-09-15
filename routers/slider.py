from fastapi import APIRouter, Depends, UploadFile, File, Form
from services import sliders
# from models.slider import SliderCreate
from core.auth import get_current_user

router = APIRouter(
    prefix="/sliders",
    tags=["sliders"]
)

@router.post("", dependencies=[Depends(get_current_user)])
async def create_slider(
    title: str = Form(...),           # form field
    image: UploadFile = File(...)     # file field
):
    slider_data = {
        "title": title,
        "image_path": image
    }
    return sliders.create_sliders(slider_data)

@router.get("")
def get_sliders():
    return sliders.get_all_sliders()

@router.delete("/{slider_id}")
def delete_slider(slider_id: str):
    return sliders.delete_slider(slider_id)

@router.get("/{slider_id}")
def get_slider_by_id(slider_id: str):
    return sliders.get_slider_by_id(slider_id)