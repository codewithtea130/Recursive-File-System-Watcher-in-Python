from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import sys


def get_path():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    if not folder:
        print("No Folder Selected!")
        sys.exit()
    p = Path(folder)
    if not p.exists():
        raise ValueError("Invalid Path!")
    elif not p.is_dir():
        raise ValueError("Not a Folder")

    return p.resolve()
