# Create a DataLoader class that:
# - Loads CSV files into pandas DataFrames
# - Validates the data (checks for required columns, handles missing values)
# - Performs basic data cleaning (date parsing, type conversion)
# - Has methods for filtering data by date range and categories

import pandas as pd
from datetime import datetime
from typing import List, Optional, Dict

import os

class DataLoader:
    def init(self, file_path: str, required_columns: List[str], date_column: str):
        self.file_path = file_path
        self.required_columns = required_columns
        self.date_column = date_column
        self.data = None

    def load_data(self) -> pd.DataFrame:
        """Load data from a CSV file into a pandas DataFrame."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")

        self.data = pd.read_csv(self.file_path)
        return self.data

    def validate_data(self) -> bool:
        """Validate the data for required columns and missing values."""
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Check for required columns
        missing_columns = [col for col in self.required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        # Check for missing values in required columns
        missing_values = self.data[self.required_columns].isnull().sum()
        if missing_values.any():
            raise ValueError(f"Missing values found in columns: {missing_values[missing_values > 0].index.tolist()}")

        return True