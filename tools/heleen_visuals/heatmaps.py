"""
Heatmap tools for quick correlation visualization.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df, figsize=(10, 8), annot=False):
    """
    Draws a correlation heatmap of numeric columns.
    annot=True shows correlation values.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        print("❌ No numeric columns available for correlation heatmap.")
        return

    plt.figure(figsize=figsize)
    sns.heatmap(
        numeric_df.corr(),
        cmap="coolwarm",
        annot=annot,
        fmt=".2f",
        linewidths=0.5
    )
    plt.title("Correlation Heatmap", fontsize=16)
    plt.show()
