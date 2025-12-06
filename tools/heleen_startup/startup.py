"""
Heleen Professional Startup Module
----------------------------------
Initializes a clean and reliable data environment for all your projects.

Features:
- WSL-safe environment detection
- Python path + environment validation
- Library version overview
- Professional plot styling
- Notebook safety checks
- DataFrame helper utilities
"""

import sys
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ================================================================
# 🔧 WSL DETECTION (RELIABLE FOR ALL WSL VERSIONS)
# ================================================================

def is_wsl():
    """Detect WSL across WSL1, WSL2, and updated kernels."""
    try:
        with open('/proc/version', 'r') as f:
            content = f.read().lower()
            # Works on old + new WSL kernels
            return ("microsoft" in content) or ("wsl" in content)
    except:
        return False


# ================================================================
# 🔍 ENVIRONMENT CHECK
# ================================================================

def check_environment():
    """Print Python executable and WSL detection status."""
    print("🔍 Environment Check")
    print("--------------------")
    print(f"Python executable : {sys.executable}")
    print(f"Platform          : {sys.platform}")

    if is_wsl():
        print("✅ WSL environment detected")
    else:
        print("⚠️ Could not confirm WSL — but Python path may still be correct.")
    print()


# ================================================================
# 📚 LIBRARY VERSION CHECK
# ================================================================

def check_libraries():
    """Show installed versions of major data libraries."""
    libs = {
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "seaborn": sns.__version__,
        "matplotlib": plt.matplotlib.__version__,
    }

    print("📚 Library Versions")
    print("-------------------")
    for lib, version in libs.items():
        print(f"{lib:<10} : {version}")
    print()


# ================================================================
# 🔒 NOTEBOOK SAFETY CHECK
# ================================================================

def notebook_safety(expected_folder="data_learning"):
    """Warn if notebook runs from an unexpected location."""
    cwd = os.getcwd()

    print("🔒 Notebook Safety Check")
    print("------------------------")
    print(f"Current working directory: {cwd}")

    if expected_folder not in cwd:
        print(f"⚠️ WARNING: Notebook is not inside '{expected_folder}'.")
    else:
        print("✅ Notebook is inside the expected working directory.")
    print()


# ================================================================
# 🎨 PROFESSIONAL PLOT STYLE
# ================================================================

def set_plot_style():
    """Apply consistent, professional visualization style."""
    sns.set_theme(
        style="whitegrid",
        context="talk",
        palette="deep"
    )
    print("🎨 Plot style applied.\n")


# ================================================================
# 🔎 DATAFRAME HELPERS
# ================================================================

def df_info(df, rows=5):
    """Compact DataFrame summary (shape + preview)."""
    print(f"🔎 DataFrame shape: {df.shape}")
    display(df.head(rows))


def preview(df, rows=5):
    """Simple preview helper."""
    display(df.head(rows))


# ================================================================
# 🚀 MAIN STARTUP FUNCTION
# ================================================================

def start():
    """Initialize the full Heleen Professional Analysis Environment."""

    print("\n🚀 Heleen Professional Environment Initializing...\n")

    check_environment()
    check_libraries()
    set_plot_style()
    notebook_safety()

    print("✨ Custom helpers ready:")
    print("   • df_info(df)")
    print("   • preview(df)")
    print("\n✅ Environment ready.\n")
