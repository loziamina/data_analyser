# Create a DataVisualizer class that takes analysis results and generates:
# - Bar charts for spending by category
# - Line charts for spending over time
# - Pie charts for spending distribution
# - Heatmaps for correlation between variables
# - Each method should support customization options (colors, titles, etc.)
# - Methods should return the figure and also have an option to save to file

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional
from matplotlib.ticker import FuncFormatter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Format y-axis as currency
formatter = FuncFormatter(lambda x, pos: f'${x:,.0f}')
sns.set(style="whitegrid")

class DataVisualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        logger.info("DataVisualizer initialized with data.")

    def bar_chart(self, x: str, y: str, title: str = "Bar Chart", xlabel: str = "", ylabel: str = "", color: str = "blue", save_path: Optional[str] = None) -> plt.Figure:
        logger.info("Generating bar chart.")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.data, x=x, y=y, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.gca().yaxis.set_major_formatter(formatter)
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Bar chart saved to {save_path}.")
        return plt.gcf()

    def line_chart(self, x: str, y: str, title: str = "Line Chart", xlabel: str = "", ylabel: str = "", color: str = "blue", save_path: Optional[str] = None) -> plt.Figure:
        logger.info("Generating line chart.")
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.data, x=x, y=y, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.gca().yaxis.set_major_formatter(formatter)
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Line chart saved to {save_path}.")
        return plt.gcf()

    def pie_chart(self, values: List[float], labels: List[str], title: str = "Pie Chart", save_path: Optional[str] = None) -> plt.Figure:
        logger.info("Generating pie chart.")
        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Pie chart saved to {save_path}.")
        return plt.gcf()

    def heatmap(self, data: pd.DataFrame, title: str = "Heatmap", save_path: Optional[str] = None) -> plt.Figure:
        logger.info("Generating heatmap.")
        plt.figure(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
        plt.title(title)
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Heatmap saved to {save_path}.")
        return plt.gcf()

    def save_figure(self, fig: plt.Figure, file_name: str) -> None:
        fig.savefig(file_name)
        logger.info(f"Figure saved to {file_name}.")
        