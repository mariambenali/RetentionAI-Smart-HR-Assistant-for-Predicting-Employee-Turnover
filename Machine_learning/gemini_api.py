from google import genai
from pydantic import BaseModel
from typing import List, Optional
from Machine_learning.model_config import GEMINI_key
from .predictor import model_predicted





class RetentionPlan(BaseModel):
    retention_plan: List[str]
    probability: float

client = genai.Client(api_key=GEMINI_key)

def pred_api(age:int , departement:str , role: str):

    # Prédiction ML
    churn_probability = model_predicted({
        "age": age,
        "departement": departement,
        "role": role
    })

    # Règle métier
    if churn_probability <= 0.5:
        return RetentionPlan(
            churn_probability=churn_probability,
            message="Risque de départ faible. Aucun plan requis."
        )

    # Appel LLM
    client = genai.Client(api_key=GEMINI_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
                Agis comme un expert RH. 

                Voici les informations sur l’employé :
                - Age : {age}
                - Département : {departement}
                - Role : {role}
                .
                .
                .
                Contexte : ce salarié a un risque élevé de "churn_probability" de départ selon le modèle ML.  

                Tache : propose 3 actions concrètes et personnalisées pour le retenir dans l’entreprise, en tenant compte de son role, sa satisfaction, sa performance et son équilibre vie professionnelle/personnelle.  
                Rédige les actions de façon claire et opérationnelle pour un manager RH. """,

        config={"response_mime_type": "application/json",
                "response_schema": RetentionPlan.model_json_schema(),
               }
    )
    llm_output = RetentionPlan.model_validate_json(
        f"""{{
            "churn_probability": {churn_probability},
            "retention_plan": {response.text},
            "message": "Plan de rétention généré"
        }}"""
    )
    
    

    return llm_output

