"""
Boxplot tools for categorical vs numeric visualization.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def boxplot(df, x, y, figsize=(10, 6)):
    """
    Draws a boxplot:
    x = categorical column
    y = numeric column
    """

    plt.figure(figsize=figsize)
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f"Boxplot: {y} by {x}")
    plt.xticks(rotation=45)
    plt.show()