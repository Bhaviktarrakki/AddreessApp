from pydantic import BaseModel

class Address(BaseModel):
    latitude: float
    longitude: float
    street: str
    city: str
    state: str
    zip_code: int