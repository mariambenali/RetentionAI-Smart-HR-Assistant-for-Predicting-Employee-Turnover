import joblib
import pandas as pd
import numpy as np


#changer le model
#transformer les features (l'entrée de endpoint =predict) au DF
#donner ces df au model pour la prediction prediction



model_path= "Machine_learning/attrition_model.pkl"

model = joblib.load(model_path)

'''
test_df = pd.DataFrame([{
    "Age": 35,
    "BusinessTravel": "Travel_Rarely",
    "Department": "Sales",
    "Education": 3,
    "EducationField": "Life Sciences",
    "EnvironmentSatisfaction": 3,
    "Gender": "Male",
    "JobInvolvement": 3,
    "JobLevel": 2,
    "JobRole": "Sales Executive",
    "JobSatisfaction": 3,
    "MaritalStatus": "Single",
    "MonthlyIncome": 5000,
    "Over18": "Y",
    "OverTime": "Yes",
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 3,
    "StockOptionLevel": 1,
    "TotalWorkingYears": 10,
    "WorkLifeBalance": 3,
    "YearsAtCompany": 5,
    "YearsInCurrentRole": 3,
    "YearsWithCurrManager": 3
    
}])
'''


def model_predicted(df_input: pd.DataFrame):

    proba= model.predict_proba(df_input)[:,1]
    return proba

#print(model_predicted(test_df))

