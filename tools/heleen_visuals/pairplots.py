
"""
Distribution tools for numeric and categorical features.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def distribution(df, column, bins=30, figsize=(10, 6)):
    """
    Draws a histogram + KDE for numeric columns.
    """

    plt.figure(figsize=figsize)
    sns.histplot(df[column], kde=True, bins=bins)
    plt.title(f"Distribution of {column}")
    plt.show()
