"""
Figure Saving Tools
-------------------
Automatically save matplotlib/seaborn figures
to the outputs/figures directory with timestamp.
"""

import os
from datetime import datetime
import matplotlib.pyplot as plt


def save_fig(name, folder="outputs/figures", dpi=300):
    """
    Saves the current matplotlib figure with:
    - automatic timestamp
    - safe file naming
    - folder existence check

    Example:
    save_fig("heatmap_salary")
    """

    # Ensure folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Safe filename
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    # Save figure
    plt.savefig(filepath, dpi=dpi, bbox_inches="tight")
    print(f"💾 Figure saved as: {filepath}")
