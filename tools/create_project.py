"""
Heleen Project Generator
------------------------
Automatically creates a full ADA-ready project structure:
- folders for data, scripts, notebooks, outputs
- starter notebook with startup + toolkit imports
- README template
"""

import os
import sys
from datetime import datetime

# ---------------------------------------------------------
# Helper: Create folder if not exists
# ---------------------------------------------------------
def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Created folder: {path}")


# ---------------------------------------------------------
# Starter notebook content
# ---------------------------------------------------------
NOTEBOOK_TEMPLATE = """\
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tools.heleen_startup.startup import start\\n",
    "start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tools\\n",
    "from tools.heleen_tools.csv_loader import load_csv\\n",
    "\\n",
    "from tools.heleen_tools.cleaning import (\\n",
    "    missing_values, duplicates, clean_column_names, drop_empty_columns,\\n",
    "    clean_whitespace, full_clean_report\\n",
    ")\\n",
    "\\n",
    "from tools.heleen_tools.summary import (\\n",
    "    df_summary, describe_extended, memory_usage, outlier_report\\n",
    ")\\n",
    "\\n",
    "from tools.heleen_tools.dtype_tools import (\\n",
    "    detect_numeric, detect_categorical, detect_text, detect_mixed_types,\\n",
    "    to_numeric_safe, to_category\\n",
    ")\\n",
    "\\n",
    "from tools.heleen_visuals.heatmaps import correlation_heatmap\\n",
    "from tools.heleen_visuals.boxplots import boxplot\\n",
    "from tools.heleen_visuals.distributions import distribution\\n",
    "from tools.heleen_visuals.pairplots import pairplot\\n",
    "from tools.heleen_visuals.save_fig import save_fig"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (main_env)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
"""


# ---------------------------------------------------------
# README template
# ---------------------------------------------------------
README_TEMPLATE = """\
# {project}

Created on {date}

## Project Structure
