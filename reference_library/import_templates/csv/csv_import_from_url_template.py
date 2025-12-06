"""
CSV Import Template: Load CSV from URL and Save Locally
-------------------------------------------------------
Gebruik deze template voor alle externe datasets
die via een URL worden ingeladen en lokaal opgeslagen.
"""

import pandas as pd
import os

# 1. Externe dataset-URL (aanpassen naar wens)
FILE_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"

# 2. Standaard opslaglocatie (pas aan naar jouw structuur)
SAVE_DIR = r"C:\Users\Beheerder\data_learning\python_data_analysis\module_1_importing_data\docs"
os.makedirs(SAVE_DIR, exist_ok=True)

# 3. Bestandsnaam afleiden uit URL of zelf invullen
FILENAME = "laptop_pricing_dataset_base.csv"
SAVE_PATH = os.path.join(SAVE_DIR, FILENAME)

def load_and_save_csv(file_url=FILE_URL, save_path=SAVE_PATH):
    """Laadt CSV vanaf URL en slaat lokaal op."""
    print(f"Downloading: {file_url}")

    try:
        df = pd.read_csv(file_url, header=None)
    except Exception as e:
        print(f"Error while downloading CSV: {e}")
        return None



if __name__ == "__main__":
    load_and_save_csv()
