import os
import shutil
import json
import hashlib
from datetime import datetime

# =====================================================================
# CONFIGURATIE
# =====================================================================

BASE_DIR = r"C:\Users\Beheerder\data_learning"

RULESET_FILE = os.path.join(BASE_DIR, "tools", "ruleset.json")
LOGFILE = os.path.join(BASE_DIR, "tools", "audit_log.txt")

DEFAULT_RULES = {
    ".csv": "datasets",
    ".xlsx": "datasets",
    ".json": "reference_library",
    ".db": "sqlite_databases",
    ".sql": "sqlite_databases",
    ".py": "python_projects",
    ".ipynb": "python_projects",
}

# =====================================================================
# HULPFUNCTIES
# =====================================================================

def color(text, c):
    """Terminal kleurcodes."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }
    return colors[c] + text + colors["reset"]


def log(msg):
    """Log naar audit_log.txt"""
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {msg}\n")


def load_ruleset():
    if not os.path.exists(RULESET_FILE):
        save_ruleset(DEFAULT_RULES)
        return DEFAULT_RULES
    with open(RULESET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_ruleset(rules):
    with open(RULESET_FILE, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=4)

# =====================================================================
# SCAN-FUNCTIES
# =====================================================================

def find_orphans(rules):
    """Bestanden die niet in de juiste map staan."""
    orphans = []

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            ext = os.path.splitext(file)[1].lower()

            if ext in rules:
                correct_folder = os.path.join(BASE_DIR, rules[ext])
                full_path = os.path.join(root, file)

                if not full_path.startswith(correct_folder):
                    orphans.append((full_path, rules[ext]))

    return orphans


def find_empty_dirs():
    """Lege mappen detecteren."""
    empty = []
    for root, dirs, files in os.walk(BASE_DIR):
        # sla bovenste map over
        if root == BASE_DIR:
            continue

        if len(files) == 0 and len(dirs) == 0:
            empty.append(root)
    return empty


def find_lost_files():
    """Bestanden zonder extensie of extreem rare extensie."""
    lost = []
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext == "" or len(ext) > 10:
                lost.append(os.path.join(root, file))
    return lost


# =====================================================================
# DUPLICATE DETECTIE
# =====================================================================

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def find_duplicates():
    """Zoek dubbele bestanden via bestandshash."""
    hash_map = {}
    duplicates = []

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                h = file_hash(file_path)
            except:
                continue

            if h not in hash_map:
                hash_map[h] = [file_path]
            else:
                hash_map[h].append(file_path)

    for h, group in hash_map.items():
        if len(group) > 1:
            duplicates.append(group)

    return duplicates


# =====================================================================
# ACTIES
# =====================================================================

def move_file(path, target):
    os.makedirs(target, exist_ok=True)
    new_path = os.path.join(target, os.path.basename(path))
    shutil.move(path, new_path)
    log(f"Moved: {path} -> {new_path}")
    print(color(f"➡ Verplaatst naar {new_path}", "green"))


def delete_file(path):
    os.remove(path)
    log(f"Deleted: {path}")
    print(color("🗑 Verwijderd.", "red"))


# =====================================================================
# INTERACTIEVE VERWERKING
# =====================================================================

def handle_file(path, target, rules):
    ext = os.path.splitext(path)[1]

    print(color("\nBestand gevonden:", "yellow"))
    print(path)
    print(f"Hoort thuis in: {target}")

    print("\nActies:")
    print("1) Verplaatsen")
    print("2) Verwijderen")
    print("3) Overslaan")
    print("4) Nieuwe regel maken voor dit bestandstype")

    c = input("\nKies (1/2/3/4): ").strip()

    if c == "1":
        move_file(path, os.path.join(BASE_DIR, target))

    elif c == "2":
        delete_file(path)

    elif c == "4":
        new_dir = input("Nieuwe doelmap: ").strip()
        rules[ext] = new_dir
        save_ruleset(rules)
        print(color("✔ Regel opgeslagen!", "green"))
        move_file(path, os.path.join(BASE_DIR, new_dir))

    else:
        print(color("⏭ Overgeslagen.", "blue"))


def auto_mode(orphans, rules):
    print(color("\nAUTO MODE", "blue"))
    for path, target in orphans:
        move_file(path, os.path.join(BASE_DIR, target))
    print(color("\n✔ Alles automatisch opgeruimd!", "green"))
