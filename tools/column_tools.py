def show_cols(df):
    for i, col in enumerate(df.columns):
        print(f"{i:02d} → {col}")
    print(f"\nTotal columns: {len(df.columns)}")


def search_cols(df, text):
    text = text.lower()
    matches = [c for c in df.columns if text in c.lower()]
    print(f'\n🔍 "{text}" gevonden in:')
    for m in matches:
        print(" -", m)
    if not matches:
        print("⚠ Geen matches gevonden.")
    return matches
def save_column_sheet(df, path="COLUMNS.md"):
    """
    Maakt automatisch een Markdown cheat sheet met alle kolomnamen.
    Perfect om op een tweede scherm te openen.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("# 📄 Column Overview\n\n")
            for i, col in enumerate(df.columns):
                f.write(f"{i:02d} → {col}  \n")
            f.write(f"\n**Total columns: {len(df.columns)}**\n")

        print(f"✅ Column sheet saved to: {path}")
    except Exception as e:
        print(f"❌ Error saving column sheet: {e}")
