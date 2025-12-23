from .database import Base, engine, get_db
from .schema import UserCreate, UserLogin, EmployeeId, CreationEmployee
from .models import User, Employee, History
from fastapi import FastAPI, Depends, HTTPException
from .hash import hashed_password, verify_password
from .security import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from Machine_learning.gemini_api import service_gemini
from sqlalchemy.orm import Session
from datetime import date
from jose import jwt
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import json


model_path= "Machine_learning/attrition_model.pkl"
model = joblib.load(model_path)



Base.metadata.create_all(bind=engine)
app = FastAPI()
type_token= HTTPBearer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(user:UserCreate, db: Session = Depends(get_db)):
    hash_password = hashed_password(user.password) 
    new_user=User (
        username= user.username,
        password= hash_password,
        date_creation= date.today()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.post("/login")
def login(user:UserLogin, db: Session = Depends(get_db)):
    user_login = db.query(User).filter(User.username == user.username).first()

    if not user_login:
        raise HTTPException(status_code = 404, detail="User not found")
    elif not verify_password(user.password, user_login.password):
        raise HTTPException(status_code=401, detail="Invalid credentials") ########### AVERIFIERRRRR !!!!!!
    
    payload = {"sub": user_login.username}
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    return token


@app.get("/token")
def get_token(token:HTTPAuthorizationCredentials = Depends(type_token)):
    try:
        decoded = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
    

@app.post("/employees")
def create_employee(employee: CreationEmployee,db: Session = Depends(get_db)):

    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee






@app.post("/prediction")
def prediction(request: EmployeeId, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(Employee.id == request.employee_id).first()
    if not employee:
        return {"error": "Employee not found"}


    employee_dict = {
        "Age": employee.age,
        "BusinessTravel": employee.business_travel,
        "Department": employee.department,
        "Education": employee.education,
        "EducationField": employee.education_field,
        "EnvironmentSatisfaction": employee.environment_satisfaction,
        "Gender": employee.gender,
        "JobInvolvement": employee.job_involvement,
        "JobLevel": employee.job_level,
        "JobRole": employee.job_role,
        "JobSatisfaction": employee.job_satisfaction,
        "MaritalStatus": employee.marital_status,
        "MonthlyIncome": employee.monthly_income,
        "Over18": employee.over18,
        "OverTime": employee.overtime,
        "PerformanceRating": employee.performance_rating,
        "RelationshipSatisfaction": employee.relationship_satisfaction,
        "StockOptionLevel": employee.stock_option_level,
        "TotalWorkingYears": employee.total_working_years,
        "WorkLifeBalance": employee.work_life_balance,
        "YearsAtCompany": employee.years_at_company,
        "YearsInCurrentRole": employee.years_in_current_role,
        "YearsWithCurrManager": employee.years_with_curr_manager
        }

    # DataFrame pour le modèle
    employee_df = pd.DataFrame([employee_dict])
    pred_attrition = model.predict_proba(employee_df)[:, 1]

    new_prediction= History(
        probability= pred_attrition.tolist()[0],
        retention_plan = None,
        employee_id = request.employee_id
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    return {"churn_probability": new_prediction}


@app.post("/generate-retention-plan")
def generate_retention(request: EmployeeId, db: Session = Depends(get_db)):

    employee_history = db.query(History).filter(History.employee_id == request.employee_id).first()

    employee = db.query(Employee).filter(Employee.id == request.employee_id).first()

    ret_probability = employee_history.probability

    if ret_probability < 0.5 and not employee_history.retention_plan:
        plan= service_gemini(employee)

        if isinstance(plan, str):
            plan_form = json.loads(plan)

        plan_form = plan.get("RetentionPlan", [])

        employee_history.retention_plan= plan_form
        

        db.commit()
        db.refresh(employee_history)

        return plan
    
    

    return {"message": "the plan already exist, check the pourcentage of probability"}










