import sys
import importlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------
# CORE CHECKS
# ---------------------------------------------------

def check_environment():
    """Controleert of Python via WSL draait en welke interpreter actief is."""
    print("🔎 Environment check:")
    print(f"   Python executable : {sys.executable}")
    print(f"   Platform           : {sys.platform}")

    if "mnt" in sys.executable or "ubuntu" in sys.executable:
        print("   ✅ WSL environment confirmed.")
    else:
        print("   ⚠️  Warning: This is NOT WSL. You may be using Windows Python!")

def check_libraries():
    """Checkt of de belangrijkste libraries correct geladen zijn."""
    libs = {
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "seaborn": sns.__version__,
        "matplotlib": plt.matplotlib.__version__,
    }

    print("\n📚 Library versions:")
    for lib, version in libs.items():
        print(f"   {lib:<10} : {version}")

# ---------------------------------------------------
# CUSTOM HELPERS
# ---------------------------------------------------

def df_info(df, rows=5):
    """Compact overzicht van shape + head."""
    print(f"\n🔹 DataFrame shape: {df.shape}")
    display(df.head(rows))

def preview(df, rows=5):
    """Alias voor df.head() maar met nette naam."""
    display(df.head(rows))

# ---------------------------------------------------
# START FUNCTION
# ---------------------------------------------------

def start():
    print("🚀 Heleen Professional Environment Loaded\n")
    check_environment()
    check_libraries()

    print("\n✨ Custom helpers ready:")
    print("   - df_info(df)")
    print("   - preview(df)")

    print("\n✅ Startup complete.\n")
