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
    Age = Column(Integer)
    BusinessTravel = Column(String)
    Department = Column(String)
    Education = Column(Integer)
    EducationField = Column(String)
    EnvironmentSatisfaction = Column(Integer)
    Gender = Column(String)
    JobInvolvement = Column(Integer)
    JobLevel = Column(Integer)
    JobRole = Column(String)
    JobSatisfaction = Column(Integer)
    MaritalStatus = Column(String)
    MonthlyIncome = Column(Integer)
    Over18 = Column(String)
    OverTime = Column(String)
    PerformanceRating = Column(Integer)
    RelationshipSatisfaction = Column(Integer)
    StockOptionLevel = Column(Integer)
    TotalWorkingYears = Column(Integer)
    WorkLifeBalance = Column(Integer)
    YearsAtCompany = Column(Integer)
    YearsInCurrentRole = Column(Integer)
    YearsWithCurrManager = Column(Integer)

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