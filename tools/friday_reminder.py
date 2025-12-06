import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

# Pad naar jouw weekly audit script
BASE_DIR = r"C:\Users\Beheerder\data_learning"
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
WEEKLY_AUDIT = os.path.join(TOOLS_DIR, "weekly_audit.py")


def main():
    # Maak de popup (zonder leeg hoofdvenster)
    root = tk.Tk()
    root.withdraw()

    message = "Wil je je Weekly Audit runnen?"

    # Vraag Ja / Nee
    run_now = messagebox.askyesno("Weekly Audit Reminder", message)

    if run_now:
        # Draai de weekly audit met dezelfde Python die dit script draait
        subprocess.run([sys.executable, WEEKLY_AUDIT])
        messagebox.showinfo("Weekly Audit", "Audit is uitgevoerd!")
    else:
        messagebox.showinfo("Weekly Audit", "Geen probleem, je kunt hem later draaien.")

    root.destroy()


if __name__ == "__main__":
    main()
