# Write tests for the DataLoader class:
# - Test that data is loaded correctly
# - Test validation of required columns
# - Test date filtering functionality
# - Test category filtering functionality
from src.analyzer import DataAnalyzer
import pandas as pd

#Données de test
df = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=6, freq='D'),
    'category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'amount': [100, 200, 300, 400, 500, 600]
})

def test_summary_statistics():
    analyzer = DataAnalyzer(df, date_column='date')
    summary = analyzer.summary_statistics(category_column='category')
    assert 'amount' in summary.columns

def test_time_series_analysis():
    analyzer = DataAnalyzer(df, date_column='date')
    ts = analyzer.time_series_analysis(value_column='amount')
    assert not ts.empty

def test_spending_distribution():
    analyzer = DataAnalyzer(df, date_column='date')
    analyzer.spending_distribution(value_column='amount')  # Ne renvoie rien, ne pas faire d'assert ici

def test_top_spending_categories():
    analyzer = DataAnalyzer(df, date_column='date')
    top = analyzer.top_spending_categories(category_column='category', value_column='amount')
    assert not top.empty

def test_customer_segmentation():
    analyzer = DataAnalyzer(df, date_column='date')
    customers = analyzer.customer_segmentation(value_columns=['amount'])
    assert 'Cluster' in customers.columns
    assert 'amount' in customers.columns

