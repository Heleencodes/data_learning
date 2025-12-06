"""
Automatic path setup for Heleen's project structure.
Ensures the tools folder is always importable.
"""

import sys
from pathlib import Path


def ensure_tools_path():
    """
    Add the 'tools' directory to sys.path automatically.
    Works no matter where the notebook is located.
    """
    cwd = Path.cwd().resolve()

    # Look for tools in current directory
    candidate_1 = cwd / "tools"

    # Look one level up
    candidate_2 = cwd.parent / "tools"

    # Look two levels up
    candidate_3 = cwd.parent.parent / "tools"

    for cand in [candidate_1, candidate_2, candidate_3]:
        if cand.exists():
            sys.path.append(str(cand))
            return str(cand)

    return None
