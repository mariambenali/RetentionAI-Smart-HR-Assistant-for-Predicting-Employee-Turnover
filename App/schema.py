from pydantic import BaseModel
from datetime import date



class UserCreate(BaseModel):
    username: str
    password: str
    date_creation: date



class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        model_config = {
            "from_attributes": True
            }


class Prediction(BaseModel):
    employee_id: int
    probability: str