from .database import Base
from sqlalchemy import String, Integer,Float,Column, Date, ForeignKey




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True)
    username = Column(String)
    password = Column(String)
    date_creation = Column(Date)
    


class Prediction(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    employee_id = Column(Integer)
    probability = Column(Integer)



