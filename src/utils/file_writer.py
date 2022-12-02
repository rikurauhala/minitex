import tkinter as tk
from tkinter import filedialog

class FileWriter:
    def __init__(self) -> None:
        self._root = tk.Tk()
        self._root.withdraw()