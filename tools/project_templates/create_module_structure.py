import os
import sys
from pathlib import Path

# ============================================
#   PRO PROJECT / MODULE STRUCTURE GENERATOR
#   Heleen — for ADA Data & Analytics Bootcamp
# ============================================

BASE_DIR = Path(__file__).resolve().parents[2]   # Goes back to /data_learning level


# --------------------------------------------
# Helper: Create folder + .gitkeep
# --------------------------------------------
def make_folder(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    gitkeep = path / ".gitkeep"
    gitkeep.touch(exist_ok=True)


# --------------------------------------------
# Create module structure
# --------------------------------------------
def create_module_structure(module_name: str):
    module_path = BASE_DIR / "projects" / module_name

    folders = [
        "data_raw",
        "data_processed",
        "notebooks",
        "scripts",
        "docs",
        "outputs"
    ]

    print(f"\n📁 Creating module structure for: {module_name}")
    print(f"→ Location: {module_path}\n")

    for folder in folders:
        full_path = module_path / folder
        make_folder(full_path)
        print(f"  ✔ {folder}")

    # README
    readme = module_path / "README.md"
    if not readme.exists():
        readme.write_text(f"# {module_name}\n\nProject module generated automatically.\n")
        print("  ✔ README.md created")

    print("\n🎉 Module structure is ready!\n")


# --------------------------------------------
# Create full data project
# --------------------------------------------
def create_full_project(project_name: str):
    project_path = BASE_DIR / "projects" / project_name

    print(f"\n📦 Creating full project: {project_name}")
    print(f"→ Location: {project_path}\n")

    project_path.mkdir(parents=True, exist_ok=True)

    # Default project folders
    folders = [
        "data",
        "notebooks",
        "scripts",
        "docs",
        "outputs",
        "sql",
        "references"
    ]

    for folder in folders:
        full_path = project_path / folder
        make_folder(full_path)
        print(f"  ✔ {folder}")

    readme = project_path / "README.md"
    if not readme.exists():
        readme.write_text(f"# {project_name}\n\nGenerated project skeleton.\n")
        print("  ✔ README.md created")

    print("\n🎉 Project structure is ready!\n")


# --------------------------------------------
# Interactive CLI
# --------------------------------------------
def main():
    print("\n🚀 Heleen’s Project/Module Generator")
    print("-----------------------------------")
    print("1. Create new DATA MODULE (recommended)")
    print("2. Create full DATA PROJECT")
    print("3. Exit\n")

    choice = input("Select option (1/2/3): ")

    if choice == "1":
        module_name = input("\nModule name (e.g., module_3_data_cleaning): ").strip()
        create_module_structure(module_name)

    elif choice == "2":
        project_name = input("\nProject name: ").strip()
        create_full_project(project_name)

    else:
        print("\nBye! 👋")
        sys.exit()


if __name__ == "__main__":
    main()
