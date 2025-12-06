import os
from datetime import datetime

from map_auditor_core import (
    BASE_DIR,
    load_ruleset,
    find_orphans,
    find_empty_dirs,
    find_lost_files,
    find_duplicates,
)

# ---------------------------------------------------------
# Config
# ---------------------------------------------------------

TOOLS_DIR = os.path.join(BASE_DIR, "tools")
REPORT_DIR = os.path.join(TOOLS_DIR, "audit_reports")
os.makedirs(REPORT_DIR, exist_ok=True)

# ---------------------------------------------------------
# Hulpfuncties: samenvatting + PDF
# ---------------------------------------------------------


def build_summary():
    """Draait alle checks en geeft een dict terug met resultaten."""
    rules = load_ruleset()

    orphans = find_orphans(rules)
    empty_dirs = find_empty_dirs()
    lost_files = find_lost_files()
    duplicates = find_duplicates()

    summary = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "base_dir": BASE_DIR,
        "orphans_count": len(orphans),
        "empty_dirs_count": len(empty_dirs),
        "lost_files_count": len(lost_files),
        "duplicate_groups_count": len(duplicates),
        "orphans": orphans,
        "empty_dirs": empty_dirs,
        "lost_files": lost_files,
        "duplicates": duplicates,
    }
    return summary


def write_txt_summary(summary, path):
    """Schrijf een simpele tekstsamenvatting naast de PDF."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Weekly Audit - {summary['timestamp']}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Basis-map: {summary['base_dir']}\n\n")
        f.write(f"Verdwaalde bestanden: {summary['orphans_count']}\n")
        f.write(f"Lege mappen:           {summary['empty_dirs_count']}\n")
        f.write(f"Rare / extensieloze:   {summary['lost_files_count']}\n")
        f.write(f"Duplicaat-groepen:     {summary['duplicate_groups_count']}\n\n")

        def block(title, items, limit=10):
            f.write(title + "\n")
            f.write("-" * len(title) + "\n")
            if not items:
                f.write("  (niets)\n\n")
                return
            for i, item in enumerate(items[:limit], 1):
                if isinstance(item, tuple):
                    f.write(f"  {i}. {item[0]} -> hoort in {item[1]}\n")
                else:
                    f.write(f"  {i}. {item}\n")
            if len(items) > limit:
                f.write(f"  ... (+{len(items) - limit} meer)\n")
            f.write("\n")

        block("Verdwaalde bestanden", summary["orphans"])
        block("Lege mappen", summary["empty_dirs"])
        block("Rare / extensieloze bestanden", summary["lost_files"])

        # duplicates is lijst van lijsten
        f.write("Duplicaat-groepen\n")
        f.write("------------------\n")
        if not summary["duplicates"]:
            f.write("  (geen)\n")
        else:
            for idx, group in enumerate(summary["duplicates"][:5], 1):
                f.write(f"  Groep {idx}:\n")
                for path in group:
                    f.write(f"    - {path}\n")
                if idx == 5 and len(summary["duplicates"]) > 5:
                    f.write(f"    ... (+{len(summary['duplicates']) - 5} meer groepen)\n")
                    break


def write_pdf_summary(summary, path):
    """
    Maakt een simpele PDF met de belangrijkste info.
    Vereist:  pip install fpdf2
    """
    try:
        from fpdf import FPDF
    except ImportError:
        print("Let op: fpdf2 niet geïnstalleerd. PDF wordt overgeslagen.")
        print("Installeer met: pip install fpdf2")
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Weekly Audit Report", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Datum: {summary['timestamp']}", ln=1)
    pdf.cell(0, 8, f"Basis-map: {summary['base_dir']}", ln=1)
    pdf.ln(5)

    # Tabel met aantallen
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Samenvatting", ln=1)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 6, f"Verdwaalde bestanden: {summary['orphans_count']}", ln=1)
    pdf.cell(0, 6, f"Lege mappen:           {summary['empty_dirs_count']}", ln=1)
    pdf.cell(0, 6, f"Rare/extensieloze:    {summary['lost_files_count']}", ln=1)
    pdf.cell(0, 6, f"Duplicaat-groepen:    {summary['duplicate_groups_count']}", ln=1)
    pdf.ln(5)

    # Helper voor lijstblokken
    def block(title, items, limit=8):
        pdf.set_font("Arial", "B", 12)
        # titel altijd vanaf linkermarge
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 8, title, ln=1)

        pdf.set_font("Arial", "", 10)
        page_width = pdf.w - pdf.l_margin - pdf.r_margin  # bruikbare breedte

        if not items:
            pdf.set_x(pdf.l_margin)
            pdf.cell(0, 5, "(niets)", ln=1)
            pdf.ln(2)
            return

        for i, item in enumerate(items[:limit], 1):
            if isinstance(item, tuple):
                txt = f"{i}. {os.path.basename(item[0])} -> {item[1]}"
            else:
                txt = f"{i}. {os.path.basename(item)}"
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(page_width, 5, txt)

        if len(items) > limit:
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(
                page_width,
                5,
                f"... (+{len(items) - limit} meer)",
            )

        pdf.ln(3)

    block("Verdwaalde bestanden (voorbeeld)", summary["orphans"])
    block("Lege mappen (voorbeeld)", summary["empty_dirs"])
    block("Rare / extensieloze bestanden (voorbeeld)", summary["lost_files"])

    pdf.output(path)


def run_weekly_audit():
    summary = build_summary()

    ts = datetime.now().strftime("%Y%m%d_%H%M")
    base_name = f"weekly_audit_{ts}"
    txt_path = os.path.join(REPORT_DIR, base_name + ".txt")
    pdf_path = os.path.join(REPORT_DIR, base_name + ".pdf")

    write_txt_summary(summary, txt_path)
    write_pdf_summary(summary, pdf_path)

    print("\n✅ Weekly Audit afgerond.")
    print(f"- TXT rapport: {txt_path}")
    if os.path.exists(pdf_path):
        print(f"- PDF rapport: {pdf_path}")
    else:
        print("- PDF kon niet gemaakt worden (waarschijnlijk fpdf2 niet geïnstalleerd).")


if __name__ == "__main__":
    run_weekly_audit()
