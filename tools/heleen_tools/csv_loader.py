"""
CSV Loader Tools
----------------
Safe and convenient tools for loading CSV files in Heleen's projects.
"""

import os
import pandas as pd

# Auto-detect encodings
TRY_ENCODINGS = [
    "utf-8",
    "latin1",
    "ISO-8859-1",
    "windows-1252",
]

def load_csv(path, verbose=True):
    """
    Safe CSV loading with:
    - file existence check
    - encoding fallback
    - readable error messages
    - dataframe preview
    """

    if verbose:
        print(f"\n📄 Loading CSV: {path}")

    # ---- File exists? ----
    if not os.path.exists(path):
        print(f"❌ ERROR: File does not exist: {path}")
        return None

    # ---- Try encodings ----
    for enc in TRY_ENCODINGS:
        try:
            df = pd.read_csv(path, encoding=enc)
            if verbose:
                print(f"✅ Successfully loaded with encoding: {enc}")
                print(f"🔢 Shape : {df.shape}")
                print(f"🔠 Columns: {list(df.columns)}")
            return df

        except Exception:
            continue

    print("❌ ERROR: Failed to load CSV with common encodings.")
    return None
