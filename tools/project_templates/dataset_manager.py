import os
import re
import shutil
import pandas as pd
from datetime import datetime

# ====================================================
# CONFIG — pas alleen aan als jij dat wilt
# ====================================================
BASE_DIR = r"C:\Users\Beheerder\data_learning\datasets"
RAW_DIR = os.path.join(BASE_DIR, "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
FINAL_DIR = os.path.join(BASE_DIR, "final")
README_PATH = os.path.join(BASE_DIR, "README_datasets.md")

# Naamconventie: domain_subject_detail_raw.csv
NAMING_PATTERNS = {
    "chicago": "education_chicago_public_schools_raw.csv",
    "dagelijkse": "productivity_dagelijkse_tijdregistratie_2025.xlsx",
    "topselling": "music_top_selling_albums_raw.csv",
}

# ====================================================
# Helpers
# ====================================================
def ensure_directories():
    for folder in [RAW_DIR, PROCESSED_DIR, FINAL_DIR]:
        os.makedirs(folder, exist_ok=True)


def normalize_filename(name):
    """Converts a file name to a clean lowercase, underscore-only version."""
    name = name.lower()
    name = name.replace(" ", "_")
    name = re.sub(r"[^a-z0-9_.]", "", name)
    return name


def map_to_new_name(filename):
    """Match known datasets based on keywords."""
    filename_lower = filename.lower()

    for key, newname in NAMING_PATTERNS.items():
        if key in filename_lower:
            return newname

    # If unknown file → auto-generate name
    base = normalize_filename(os.path.splitext(filename)[0])
    ext = filename.split(".")[-1]
    today = datetime.now().strftime("%Y%m%d")

    return f"misc_{base}_{today}.{ext}"


def move_and_rename():
    moved_files = []

    for file in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, file)

        # Skip directories
        if os.path.isdir(path):
            continue

        new_name = map_to_new_name(file)
        destination = os.path.join(RAW_DIR, new_name)

        shutil.move(path, destination)

        moved_files.append((file, new_name))

    return moved_files


def validate_dataset(filepath):
    ext = filepath.split(".")[-1]

    if ext == "csv":
        try:
            pd.read_csv(filepath, nrows=5)
            return True
        except Exception:
            return False

    if ext in ["xls", "xlsx"]:
        try:
            pd.read_excel(filepath, nrows=5)
            return True
        except Exception:
            return False

    return False


def generate_readme():
    lines = []
    lines.append("# 📘 Dataset Catalog — data_learning/datasets/\n")

    for fname in os.listdir(RAW_DIR):
        file_path = os.path.join(RAW_DIR, fname)
        valid = validate_dataset(file_path)

        lines.append(f"## {fname}")
        lines.append(f"- **Locatie:** raw/")
        lines.append(f"- **Geldig bestand:** {'✔️ Ja' if valid else '❌ Fout'}")
        lines.append(f"- **Laatst gewijzigd:** {datetime.fromtimestamp(os.path.getmtime(file_path))}")
        lines.append("")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ====================================================
# MAIN EXECUTION
# ====================================================
if __name__ == "__main__":
    print("📂 Dataset manager gestart...\n")

    ensure_directories()
    moved = move_and_rename()
    generate_readme()

    print("🔄 Verwerkte bestanden:")
    for old, new in moved:
        print(f"   {old}  →  {new}")

    print("\n📄 README_datasets.md bijgewerkt.")
    print("✅ Klaar!")
