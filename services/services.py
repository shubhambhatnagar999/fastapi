from database import db
from bson import ObjectId
from fastapi import Query, HTTPException

def get_all_services():
    services = list(db['services'].find({}))
    for service in services:
        service["_id"] = str(service["_id"])
    return services

def get_service_by_id(service_id: str):
    try:
        obj_id = ObjectId(service_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid service ID")

    service = db['services'].find_one({"_id": obj_id})
    service["_id"] = str(service["_id"])
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")    
    return service

def create_service(service):
    service_dict = service.dict()
    result = db['services'].insert_one(service_dict)
    service_dict["_id"] = str(result.inserted_id)
    return service_dict

def delete_service(service_id: str):
    try:
        obj_id = ObjectId(service_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid service ID")

    result = db['services'].delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}