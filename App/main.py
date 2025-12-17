from .database import Base, engine, get_db
from .schema import UserCreate, UserLogin, Prediction
from .models import User, Employee
from fastapi import FastAPI, Depends, HTTPException
from .hash import hashed_password, verify_password
from .security import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
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