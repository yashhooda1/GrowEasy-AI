import pandas as pd

class DataIngestion:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_data(self):
        """Load data from CSV, JSON, or Excel."""
        if self.file_path.endswith('.csv'):
            return pd.read_csv(self.file_path)
        elif self.file_path.endswith('.json'):
            return pd.read_json(self.file_path)
        elif self.file_path.endswith(('.xlsx', '.xls')):
            return pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format")