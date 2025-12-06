"""
Data Stack Check — PRO Version
------------------------------
Geeft uitgebreide informatie over:
- Actieve Python-versie
- Environment/location
- Aantal geïnstalleerde packages
- Tests van belangrijke data-analyse libraries
- Duidelijke ✔/❌ indicatoren

Perfect voor debugging, meerdere environments of nieuwe installs.
"""

import importlib
import sys
import pkgutil
import platform
import os


# -----------------------------------------
# Config: libraries die gecontroleerd worden
# -----------------------------------------
LIBRARIES = [
    "pandas",
    "numpy",
    "scipy",
    "seaborn",
    "matplotlib",
    "sklearn",
    "requests",
    "statsmodels",
]


GREEN = "\u2705"   # ✔
RED = "\u274C"     # ❌
YELLOW = "\u26A0"  # ⚠


def check_library(lib_name):
    """Checkt of bibliotheek geïnstalleerd is en toont versie."""
    try:
        module = importlib.import_module(lib_name)
        version = getattr(module, "__version__", "onbekende versie")
        return f"{GREEN} {lib_name:<12} versie: {version}"
    except ImportError:
        return f"{RED} {lib_name:<12} NIET geïnstalleerd!"


def main():
    print("=" * 70)
    print("PYTHON DATA STACK CHECK — PRO VERSION")
    print("=" * 70)

    # Python info
    print("\n📌 Python omgeving")
    print("-" * 70)
    print(f"Python versie   : {sys.version.split()[0]}")
    print(f"Interpreter pad : {sys.executable}")
    print(f"OS              : {platform.system()} {platform.release()}")

    # Count installed packages
    package_count = len(list(pkgutil.iter_modules()))
    print(f"Packages actief : {package_count}")

    # Libraries
    print("\n📚 Data libraries check")
    print("-" * 70)
    for lib in LIBRARIES:
        print(check_library(lib))

    print("\nKlaar. Voeg libraries toe aan de lijst als je meer wilt testen.")
    print("=" * 70)


if __name__ == "__main__":
    main()
