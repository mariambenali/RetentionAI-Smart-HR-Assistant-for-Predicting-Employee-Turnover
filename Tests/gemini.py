import pytest
from unittest.mock import patch, MagicMock
from Machine_learning.gemini_api import pred_api, RetentionPlan

#  Cas churn_probability faible (moins de 0.5)
@patch("Machine_learning.gemini_api.model_predicted")
def test_pred_api_low_churn(mock_model):
    
    #ML low probability
    mock_model.return_value = 0.3

    result = pred_api(age=30, departement="IT", role="Developer")

    assert isinstance(result, RetentionPlan)
    assert result.retention_plan is None
    assert "faible" in result.message.lower()
    assert result.probability == 0.3

# cas churn_probability élevé ( plus de 0.5)

@patch("Machine_learning.gemini_api.model_predicted")
@patch("Machine_learning.gemini_api.client")
def test_pred_api_high_churn(mock_client, mock_model):

    # ML high probability
    mock_model.return_value = 0.8

    # On simule le LLM
    fake_response = MagicMock()
    fake_response.text = '["proposer télétravail", "plan formation personnalisé"]'
    mock_client.models.generate_content.return_value = fake_response

    result = pred_api(age=40, departement="HR", role="Manager")

    assert isinstance(result, RetentionPlan)
    assert isinstance(result.retention_plan, list)
    assert len(result.retention_plan) == 3
    assert result.probability == 0.8
    assert "Plan de rétention généré" in result.message
