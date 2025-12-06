"""
Heleen Cleaning Toolkit
-----------------------
Reusable data cleaning utilities for structured datasets.
"""

import pandas as pd


# ---------------------------------------------------------
# 1. MISSING VALUES SUMMARY
# ---------------------------------------------------------
def missing_values(df):
    """
    Returns a DataFrame with:
    - total missing values
    - percentage missing per column
    """

    mv = df.isna().sum()
    pct = df.isna().mean() * 100

    report = pd.DataFrame({
        "missing_count": mv,
        "missing_pct": pct.round(2)
    })

    return report.sort_values("missing_pct", ascending=False)


# ---------------------------------------------------------
# 2. DUPLICATES SUMMARY
# ---------------------------------------------------------
def duplicates(df):
    """
    Returns the number of duplicated rows in the dataset.
    """
    return df.duplicated().sum()


# ---------------------------------------------------------
# 3. COLUMN NAME CLEANING
# ---------------------------------------------------------
def clean_column_names(df):
    """
    Lowercases + replaces spaces with underscores + strips whitespace.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^0-9a-zA-Z_]", "", regex=True)
    )
    return df


# ---------------------------------------------------------
# 4. DROP EMPTY COLUMNS
# ---------------------------------------------------------
def drop_empty_columns(df, threshold=0.98):
    """
    Removes columns that are almost completely empty.
    threshold = percentage NaN allowed (0.98 = drop columns with >98% missing).
    """
    df = df.copy()
    na_pct = df.isna().mean()
    cols_to_drop = na_pct[na_pct > threshold].index.tolist()
    return df.drop(columns=cols_to_drop), cols_to_drop


# ---------------------------------------------------------
# 5. WHITESPACE CLEANING
# ---------------------------------------------------------
def clean_whitespace(df):
    """
    Strips whitespace from string/object columns.
    """
    df = df.copy()
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()
    return df


# ---------------------------------------------------------
# 6. FULL CLEANING PIPELINE + REPORT
# ---------------------------------------------------------
def full_clean_report(df):
    """
    Runs all cleaning checks and returns a report dict:
    - missing values per column
    - duplicate rows
    - columns removed due to emptiness
    """

    report = {}

    # Missing values
    report["missing_values"] = missing_values(df)

    # Duplicates
    report["duplicate_rows"] = duplicates(df)

    # Empty columns
    _, cols_dropped = drop_empty_columns(df)
    report["empty_columns_removed"] = cols_dropped

    return report
