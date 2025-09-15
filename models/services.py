from pydantic import BaseModel

class ServiceCreate(BaseModel):
    title: str
    description: str