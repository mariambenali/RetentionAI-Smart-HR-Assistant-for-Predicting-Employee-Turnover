from .database import Base, engine, get_db
from .schema import UserCreate, UserLogin, Prediction
from .models import User, Employee
from fastapi import FastAPI, Depends, HTTPException
from .hash import hashed_password
from sqlalchemy.orm import Session
from datetime import date




Base.metadata.create_all(bind=engine)
app = FastAPI()

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


@app.get("/login")
def login(user:UserLogin, db: Session = Depends(get_db)):
    user_login = db.query(User).filter(User.username == user.username)

    if not user_login:
        raise HTTPException(status_code = 404, detail="User not found")
    elif not verify_password(user.password, user_login.hashed_password)

    return user_login

    