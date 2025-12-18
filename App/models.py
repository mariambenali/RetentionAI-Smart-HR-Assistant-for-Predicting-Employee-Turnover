from .database import Base
from sqlalchemy import String, Integer,Column, Date, ForeignKey




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True)
    username = Column(String)
    password = Column(String)
    date_creation = Column(Date)
    
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, )

    job_level = Column(Integer)
    monthly_income = Column(Integer)
    stock_option_level = Column(Integer)
    total_working_years = Column(Integer)
    years_at_company = Column(Integer)
    years_in_current_role = Column(Integer)
    years_with_curr_manager = Column(Integer)
    gender = Column(String)
    education = Column(String)
    job_satisfaction = Column(String)
    overtime = Column(String)
    relationship_satisfaction = Column(String)
    job_involvement = Column(String)
    job_role = Column(String)
    performance_rating = Column(String)
    marital_status = Column(String)
    department = Column(String)
    over_18 = Column(String)
    work_life_balance = Column(String)
    business_travel = Column(String)
    environment_satisfaction = Column(String)
    attirition = Column(String)




