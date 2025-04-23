# Create a command-line interface that:
# - Takes a CSV file path as input
# - Allows selecting analysis type (summary, time-series, category, etc.)
# - Allows selecting visualization type
# - Supports saving results to files
# - Has a help menu explaining functionality

import argparse
import os
import pandas as pd
from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer
from matplotlib import pyplot as plt

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Data Analysis Tool with Visualization")
    parser.add_argument("csv_path", type=str, help="Path to the CSV file")
    parser.add_argument("--analysis", type=str, choices=["summary", "time-series", "top-categories"], help="Type of analysis to perform")
    parser.add_argument("--plot", type=str, choices=["bar", "line", "pie", "heatmap"], help="Type of visualization to generate")
    parser.add_argument("--output", type=str, help="Path to save the generated plot (optional)")
    args = parser.parse_args()

    # Load & validate data
    required_columns = ["date", "category", "amount", "customer_id"]
    loader = DataLoader(args.csv_path, required_columns, "date")
    loader.load_data()
    loader.validate_data()
    df = loader.data

    # Analyze data
    analyzer = DataAnalyzer(df, date_column="date")

    if args.analysis == "summary":
        result = analyzer.summary_statistics(category_column="category")
        print("\n📊 Summary Statistics:\n", result)

    elif args.analysis == "time-series":
        result = analyzer.time_series_analysis(value_column="amount")
        print("\n📈 Time-Series Data:\n", result)

    elif args.analysis == "top-categories":
        result = analyzer.top_spending_categories(category_column="category", value_column="amount")
        print("\n🏆 Top Spending Categories:\n", result)
    else:
        result = df  # fallback to raw data

    # Create output directory if needed
    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Visualize
    if args.plot:
        viz = DataVisualizer(result)

        if args.plot == "bar":
            fig = viz.bar_chart(x='category', y='amount', title='Bar Chart', save_path=args.output)

        elif args.plot == "line":
            if "date" in result.columns and "amount" in result.columns:
                fig = viz.line_chart(x='date', y='amount', title='Line Chart', save_path=args.output)
            else:
                print("❌ Line chart requires 'date' and 'amount' columns.")

        elif args.plot == "pie":
            if "category" in result.columns and "amount" in result.columns:
                fig = viz.pie_chart(values=result['amount'].tolist(), labels=result['category'].tolist(), title='Pie Chart', save_path=args.output)
            else:
                print("❌ Pie chart requires 'category' and 'amount' columns.")

        elif args.plot == "heatmap":
            fig = viz.heatmap(data=result.select_dtypes(include="number"), title='Heatmap', save_path=args.output)

        # If no output path is specified, show the plot
        if not args.output:
            plt.show()

if __name__ == "__main__":
    main()
