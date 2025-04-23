# Write tests for the DataLoader class:
# - Test that data is loaded correctly
# - Test validation of required columns
# - Test date filtering functionality
# - Test category filtering functionality

import matplotlib
matplotlib.use('Agg') 

import pandas as pd
import matplotlib.pyplot as plt
from src.visualizer import DataVisualizer

df = pd.DataFrame({
    'category': ['A', 'B', 'C'],
    'amount': [100, 200, 150],
    'date': pd.date_range(start='2023-01-01', periods=3, freq='D')
})

def test_bar_chart():
    viz = DataVisualizer(df)
    fig = viz.bar_chart(x='category', y='amount')
    assert isinstance(fig, plt.Figure)

def test_line_chart():
    viz = DataVisualizer(df)
    fig = viz.line_chart(x='date', y='amount')
    assert isinstance(fig, plt.Figure)

def test_pie_chart():
    viz = DataVisualizer(df)
    fig = viz.pie_chart(values=df['amount'].tolist(), labels=df['category'].tolist())
    assert isinstance(fig, plt.Figure)

def test_heatmap():
    viz = DataVisualizer(df)
    fig = viz.heatmap(data=df[['amount']])
    assert isinstance(fig, plt.Figure)
