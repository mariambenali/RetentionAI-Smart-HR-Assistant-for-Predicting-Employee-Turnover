from .database import Base, engine, get_db
from .schema import UserCreate, UserLogin, Prediction
from .models import User, Employee
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date




Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/register")
def register(user:UserCreate, db: Session = Depends(get_db)):
    new_user=User (
        username= user.username,
        password= user.password,
        date_creation= date.today()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/login")
def login(user:UserLogin, db: Session = Depends(get_db)):
    pass