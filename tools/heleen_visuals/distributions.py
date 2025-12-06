"""
Pairplot tools for multivariate visualization.
"""

import seaborn as sns

def pairplot(df, hue=None):
    """
    Creates a Seaborn pairplot for all numeric columns.
    Optional: hue for grouping.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        print("❌ No numeric columns available for pairplot.")
        return

    sns.pairplot(df, hue=hue, diag_kind="kde")
