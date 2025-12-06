"""
Heleen Summary Toolkit
----------------------
Professional summary tools for exploratory data analysis.
"""

import pandas as pd


# ---------------------------------------------------------
# 1. BASIC SUMMARY
# ---------------------------------------------------------
def df_summary(df):
    """
    Returns:
    - column dtype
    - number of unique values
    - missing values count
    - missing percentage
    - example value
    """

    summary = pd.DataFrame({
        "dtype": df.dtypes,
        "unique_values": df.nunique(),
        "missing_count": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2),
        "example_value": df.apply(lambda col: col.dropna().iloc[0] if col.dropna().size else None)
    })

    return summary


# ---------------------------------------------------------
# 2. DESCRIBE EXTENDED
# ---------------------------------------------------------
def describe_extended(df):
    """
    More complete version of df.describe(), including:
    - numeric describe
    - object counts
    - top categories
    """
    numeric_desc = df.describe(include='number').T
    object_desc = df.describe(include='object').T

    return {
        "numeric": numeric_desc,
        "categorical": object_desc
    }


# ---------------------------------------------------------
# 3. MEMORY USAGE
# ---------------------------------------------------------
def memory_usage(df):
    """
    Returns the memory usage of each column in KB.
    """
    mem = (df.memory_usage(deep=True) / 1024).round(2)
    return mem.to_frame(name="memory_KB")


# ---------------------------------------------------------
# 4. OUTLIER CHECK (Z-SCORE)
# ---------------------------------------------------------
def outlier_report(df, threshold=3):
    """
    Detects outliers using z-score threshold.
    Only works on numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return "No numeric columns available."

    z_scores = (numeric_df - numeric_df.mean()) / numeric_df.std()
    outliers = (z_scores.abs() > threshold).sum()

    return outliers.to_frame(name="outlier_count")
