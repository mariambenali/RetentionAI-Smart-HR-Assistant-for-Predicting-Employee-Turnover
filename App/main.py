from .database import Base, engine, get_db
from .schema import UserCreate, UserLogin, Prediction, CreationEmployee
from .models import User, Employee
from fastapi import FastAPI, Depends, HTTPException
from .hash import hashed_password, verify_password
from .security import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from Machine_learning.gemini_api import pred_api
from sqlalchemy.orm import Session
from datetime import date
from jose import jwt




Base.metadata.create_all(bind=engine)
app = FastAPI()
type_token= HTTPBearer()

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
        raise HTTPException(status_code=401, detail="Invalid password")
    
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

    new_employee = Employee(**employee.dict(by_alias=False))

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@app.post("/prediction")
def prediction(pred:Prediction, db: Session = Depends(get_db)):

    pred_attirition= pred_api()

    db.add(pred_attirition)
    db.commit()
    db.refresh(pred_attirition)

    return pred_attirition