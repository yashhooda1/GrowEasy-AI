import shap
import pandas as pd

class Explainability:
    def __init__(self, model, data):
        self.model = model
        self.data = data
    
    def explain_prediction(self, X):
        """Generate SHAP-based explanation for a prediction."""
        explainer = shap.Explainer(self.model, self.data)
        shap_values = explainer(X)
        explanation = "The prediction is influenced by:\n"
        for feature, value in zip(self.data.columns, shap_values.values[0]):
            explanation += f"- {feature}: {value:.2f} impact\n"
        return explanation