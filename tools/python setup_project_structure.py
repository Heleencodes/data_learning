import os

# ---------------------------------------------------------
# Heleen's Professional Project Structure Generator
# ---------------------------------------------------------

PROJECT_ROOT = os.getcwd()

FOLDERS = [
    "tools",
    "tools/heleen_startup",
    "tools/heleen_tools",
    "tools/heleen_visuals",
    "data",
    "data/raw",
    "data/processed",
    "data/intermediate",
    "notebooks",
    "outputs",
    "outputs/figures",
    "outputs/reports",
    "scripts"
]

FILES = {
    "tools/__init__.py": "",
    "tools/heleen_startup/__init__.py": "",
    "tools/heleen_tools/__init__.py": "",
    "tools/heleen_visuals/__init__.py": "",
    "scripts/__init__.py": "",
}

def create_project_structure():
    print("\n📁 Creating project structure...\n")

    for folder in FOLDERS:
        folder_path = os.path.join(PROJECT_ROOT, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"📂 Created folder: {folder}")

    for file_path, content in FILES.items():
        abs_path = os.path.join(PROJECT_ROOT, file_path)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📄 Created file: {file_path}")

    print("\n✨ DONE: Project structure is ready!\n")
    print("Your project is now organized in a clean, ADA-ready way.\n")


if __name__ == "__main__":
    create_project_structure()
