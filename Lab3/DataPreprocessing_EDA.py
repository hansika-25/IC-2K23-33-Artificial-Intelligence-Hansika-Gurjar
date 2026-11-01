
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_dataset():
    """Create a sample student performance dataset."""
    data = {
        "Student": ["A", "B", "C", "D", "E", "F"],
        "Age": [20, 21, np.nan, 22, 20, 21],
        "Study_Hours": [2, 4, 3, np.nan, 5, 4],
        "Marks": [45, 70, 60, 80, 90, 70]
    }

    return pd.DataFrame(data)


def preprocess_data(df):
    """Handle missing values and duplicate records."""
    print("\nMissing values before preprocessing:")
    print(df.isnull().sum())

    # Replace missing numerical values with column means
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Study_Hours"] = df["Study_Hours"].fillna(
        df["Study_Hours"].mean()
    )

    # Remove duplicate records
    df = df.drop_duplicates()

    return df


def perform_eda(df):
    """Display summary statistics and explore the dataset."""
    print("\nDataset after preprocessing:")
    print(df)

    print("\nDataset Information:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nCorrelation Matrix:")
    print(df[["Age", "Study_Hours", "Marks"]].corr())


def visualize_data(df):
    """Create visualizations for exploratory data analysis."""

    # Bar chart: Student marks
    plt.figure(figsize=(8, 5))
    plt.bar(df["Student"], df["Marks"])
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.title("Student Performance")
    plt.tight_layout()
    plt.show()

    # Scatter plot: Study hours vs marks
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Study_Hours"], df["Marks"])
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.title("Study Hours vs Marks")
    plt.tight_layout()
    plt.show()


def main():
    df = create_dataset()

    print("Original Dataset:")
    print(df)

    df = preprocess_data(df)

    perform_eda(df)

    visualize_data(df)


if __name__ == "__main__":
    main()
