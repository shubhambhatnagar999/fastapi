from fastapi import APIRouter, Depends
from services import services
from models.services import ServiceCreate
from core.auth import get_current_user

router = APIRouter(
    prefix="/services",
    tags=["services"]
)

@router.get("", dependencies=[Depends(get_current_user)])
def get_services():
    return services.get_all_services()

@router.get("/{service_id}", dependencies=[Depends(get_current_user)])
def get_service_by_id(service_id: str):
    return services.get_service_by_id(service_id)

@router.post("/services", dependencies=[Depends(get_current_user)])
def create_service(service: ServiceCreate):
    return services.create_service(service)

@router.delete("/services/{service_id}", dependencies=[Depends(get_current_user)])
def delete_service(service_id: str):
    return services.delete_service(service_id)