"""
Heleen Dtype Tools
------------------
Intelligent datatype detection and conversion helpers.
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# 1. TYPE DETECTION
# ---------------------------------------------------------
def detect_numeric(df):
    """Returns all numeric columns."""
    return df.select_dtypes(include=["number"]).columns.tolist()


def detect_categorical(df):
    """Returns columns with low unique count (good for categories)."""
    return [col for col in df.columns if df[col].nunique() < 20]


def detect_text(df):
    """Returns object/string columns."""
    return df.select_dtypes(include=["object"]).columns.tolist()


# ---------------------------------------------------------
# 2. SAFE CONVERSION
# ---------------------------------------------------------
def to_numeric_safe(df, columns):
    """
    Converts selected columns to numeric.
    Non-convertible values become NaN, no crash.
    """
    df = df.copy()
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def to_category(df, columns):
    """Converts columns to pandas category dtype."""
    df = df.copy()
    for col in columns:
        df[col] = df[col].astype("category")
    return df


# ---------------------------------------------------------
# 3. MIXED TYPE DETECTION
# ---------------------------------------------------------
def detect_mixed_types(df):
    """
    Detects columns containing inconsistent datatypes,
    e.g. some numbers + some strings.
    """
    mixed = []
    for col in df.columns:
        types = df[col].dropna().apply(type).unique()
        if len(types) > 1:
            mixed.append(col)
    return mixed
