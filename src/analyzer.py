# Create a DataAnalyzer class that takes a DataFrame and provides:
# - Summary statistics (mean, median, std dev by category)
# - Time series analysis (spending trends over time)
# - Spending distribution analysis
# - Top spending categories
# - Customer segmentation by spending patterns

import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataAnalyzer:
    def __init__(self, data: pd.DataFrame, date_column: str):
        self.data = data
        self.date_column = date_column
        self.data[self.date_column] = pd.to_datetime(self.data[self.date_column])
        logger.info("DataAnalyzer initialized with data and date column.")

    def summary_statistics(self, category_column: str) -> pd.DataFrame:
        """Calculate summary statistics by category."""
        logger.info("Calculating summary statistics.")
        numeric_cols = self.data.select_dtypes(include='number').columns
        summary_stats = self.data.groupby(category_column)[numeric_cols].agg(['mean', 'median', 'std'])
        return summary_stats.reset_index()

    def time_series_analysis(self, value_column: str) -> pd.DataFrame:
        """Perform time series analysis on spending trends."""
        logger.info("Performing time series analysis.")
        time_series_data = self.data.set_index(self.date_column).resample('M')[value_column].sum()
        return time_series_data.reset_index()

    def spending_distribution(self, value_column: str) -> None:
        """Visualize spending distribution."""
        logger.info("Visualizing spending distribution.")
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[value_column], bins=30, kde=True)
        plt.title('Spending Distribution')
        plt.xlabel('Spending Amount')
        plt.ylabel('Frequency')
        plt.show()

    def top_spending_categories(self, category_column: str, value_column: str, top_n: int = 10) -> pd.DataFrame:
        """Get top spending categories."""
        logger.info("Getting top spending categories.")
        top_categories = self.data.groupby(category_column)[value_column].sum().nlargest(top_n).reset_index()
        return top_categories

    def customer_segmentation(self, value_columns: List[str], n_clusters: int = 3) -> pd.DataFrame:
        """Segment customers based on spending patterns."""
        logger.info("Performing customer segmentation.")
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.data['Cluster'] = kmeans.fit_predict(self.data[value_columns])
        return self.data[['Cluster'] + value_columns]