import platform, os

def detect_tools_path():
    # Windows path
    win_path = r"C:\Users\Beheerder\data_learning\tools"
    # WSL path
    wsl_path = "/mnt/c/Users/Beheerder/data_learning/tools"
    # ADA cloud example
    ada_path = "/home/project/tools"

    if os.path.exists(wsl_path):
        return wsl_path
    if os.path.exists(win_path):
        return win_path
    if os.path.exists(ada_path):
        return ada_path
    return None

TOOL_PATH = detect_tools_path()
