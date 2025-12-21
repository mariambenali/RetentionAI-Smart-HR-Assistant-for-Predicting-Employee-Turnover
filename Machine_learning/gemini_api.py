from google import genai
from pydantic import BaseModel
from typing import List
from Machine_learning.model_config import GEMINI_key




class RetentionPlan(BaseModel):
    retention_plan: List[str]
    probability: float


client = genai.Client(api_key=GEMINI_key)


def service_gemini(employee):

    # Appel LLM
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
                Agis comme un expert RH. 

                Voici les informations sur l’employé :
                - Employee : {employee}
          
                Contexte : ce salarié a un risque élevé de départ selon le modèle ML.  

                Tache : propose 3 actions concrètes et personnalisées pour le retenir dans l’entreprise, 
                en tenant compte de son role, sa satisfaction, sa performance et son équilibre vie professionnelle/personnelle.  
                Rédige les actions de façon claire et opérationnelle pour un manager RH. 
                Rends la réponse sous forme de liste JSON de chaînes de caractères.
                Exemple : ["Action 1", "Action 2", "Action 3"]
                """,
    )

    # Convertir le texte JSON en Python list
    import json
    try:
        plan_list = json.loads(response.text)  # Gemini doit renvoyer un JSON
    except Exception:
        # fallback si JSON non valide
        plan_list = response.text.split("\n")[:3]

    return {"RetentionPlan":plan_list}