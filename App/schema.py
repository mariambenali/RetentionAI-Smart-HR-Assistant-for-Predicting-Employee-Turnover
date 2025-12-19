from pydantic import BaseModel, Field
from datetime import date, datetime



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


class CreationEmployee(BaseModel):
    age: int = Field(alias="Age")
    business_travel: str = Field(alias="BusinessTravel")
    department: str = Field(alias="Department")
    education: int = Field(alias="Education")
    education_field: str = Field(alias="EducationField")
    environment_satisfaction: int = Field(alias="EnvironmentSatisfaction")
    gender: str = Field(alias="Gender")
    job_involvement: int = Field(alias="JobInvolvement")
    job_level: int = Field(alias="JobLevel")
    job_role: str = Field(alias="JobRole")
    job_satisfaction: int = Field(alias="JobSatisfaction")
    marital_status: str = Field(alias="MaritalStatus")
    monthly_income: int = Field(alias="MonthlyIncome")
    over18: str = Field(alias="Over18")
    overtime: str = Field(alias="OverTime")
    performance_rating: int = Field(alias="PerformanceRating")
    relationship_satisfaction: int = Field(alias="RelationshipSatisfaction")
    stock_option_level: int = Field(alias="StockOptionLevel")
    total_working_years: int = Field(alias="TotalWorkingYears")
    work_life_balance: int = Field(alias="WorkLifeBalance")
    years_at_company: int = Field(alias="YearsAtCompany")
    years_in_current_role: int = Field(alias="YearsInCurrentRole")
    years_with_curr_manager: int = Field(alias="YearsWithCurrManager")

    class Config:
        allow_population_by_field_name = True

class Prediction(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    idemployee: int
    probability: str
    retention_plan: str


