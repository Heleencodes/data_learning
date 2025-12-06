"""
Data Stack Check Script
-----------------------
Controleert of de belangrijkste data-analyse libraries geïnstalleerd zijn
en toont hun versienummer.

Voeg gerust extra libraries toe als je omgeving groeit.
"""

import importlib

LIBRARIES = [
    "pandas",
    "numpy",
    "scipy",
    "seaborn",
    "matplotlib",
    "sklearn"
]

GREEN = "\u2705"  # ✔
RED = "\u274C"    # ❌
YELLOW = "\u26A0" # ⚠


def check_library(lib_name):
    """Checkt of bibliotheek geïnstalleerd is en toont versie."""
    try:
        module = importlib.import_module(lib_name)
        version = getattr(module, "__version__", "onbekende versie")
        print(f"{GREEN} {lib_name:<12} versie: {version}")
    except ImportError:
        print(f"{RED} {lib_name:<12} is NIET geïnstalleerd!")


def main():
    print("=" * 60)
    print("PYTHON DATA STACK CHECK")
    print("=" * 60)

    for lib in LIBRARIES:
        check_library(lib)

    print("\nKlaar.\nVoeg libraries toe aan de lijst bovenin als je meer wil testen.")
    print("=" * 60)


if __name__ == "__main__":
    main()
