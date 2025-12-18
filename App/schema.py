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


class Employee(BaseModel):
    Age: int
    BusinessTravel: str
    Department: str
    Education: int
    EducationField: str
    EnvironmentSatisfaction: int
    Gender: str
    JobInvolvement: int
    JobLevel: int
    JobRole: str
    JobSatisfaction: int
    MaritalStatus: str
    MonthlyIncome: int
    Over18: str
    OverTime: str
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsWithCurrManager: int


class Prediction(BaseModel):
    idemployee: int
    probability: str

