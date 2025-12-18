from .database import Base
from sqlalchemy import String, Integer,Column, Date, ForeignKey
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key =True, index=True)
    username = Column(String)
    password = Column(String)
    date_creation = Column(Date)

#relation entre les tables: chaque User peut avoir plusieur employees
    employees = relationship(
        "Employee",
        back_populates="user",
        cascade="all, delete"
    )
    
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    business_travel = Column(String)
    department = Column(String)
    education = Column(Integer)
    education_field = Column(String)
    environment_satisfaction = Column(Integer)
    gender = Column(String)
    job_involvement = Column(Integer)
    job_level = Column(Integer)
    job_role = Column(String)
    job_satisfaction = Column(Integer)
    marital_status = Column(String)
    monthly_income = Column(Integer)
    over18 = Column(String)
    overtime = Column(String)
    performance_rating = Column(Integer)
    relationship_satisfaction = Column(Integer)
    stock_option_level = Column(Integer)
    total_working_years = Column(Integer)
    work_life_balance = Column(Integer)
    years_at_company = Column(Integer)
    years_in_current_role = Column(Integer)
    years_with_curr_manager = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="employees")

    history = relationship(
        "History",
        back_populates="employee",
        cascade="all, delete"
    )


class History(Base):
    __tablename__ = "predictions_history"

    id = Column(Integer, primary_key=True)
    userid = Column(Integer)
    employeeid = Column(Integer)
    probability = Column(String)

    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship(
        "Employee",
        back_populates="history"
    )