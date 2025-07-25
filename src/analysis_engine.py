from sklearn.linear_model import LinearRegression
import pandas as pd

class AnalysisEngine:
    def __init__(self, data):
        self.data = data
    
    def forecast_sales(self, target_column='sales', time_column='date'):
        """Simple sales forecasting using linear regression."""
        X = pd.to_datetime(self.data[time_column]).map(lambda x: x.toordinal()).values.reshape(-1, 1)
        y = self.data[target_column].values
        model = LinearRegression()
        model.fit(X, y)
        future_dates = pd.date_range(start=self.data[time_column].max(), periods=30, freq='D')
        future_X = pd.to_datetime(future_dates).map(lambda x: x.toordinal()).values.reshape(-1, 1)
        predictions = model.predict(future_X)
        return pd.DataFrame({'date': future_dates, 'predicted_sales': predictions})