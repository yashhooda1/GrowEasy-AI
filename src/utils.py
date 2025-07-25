import pandas as pd
import numpy as np

def clean_data(df):
    """Clean input DataFrame by handling missing values and data types."""
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    # Convert date column to datetime if present
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Ensure numeric columns are properly typed
    for col in df.select_dtypes(include=['object']).columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
    
    return df

def format_currency(value):
    """Format a number as currency (USD)."""
    return f"${value:,.2f}"

def validate_data(df, required_columns=['date', 'sales']):
    """Validate that the DataFrame contains required columns and valid data."""
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    if df['sales'].isna().all():
        raise ValueError("Sales column contains no valid data")
    
    return True