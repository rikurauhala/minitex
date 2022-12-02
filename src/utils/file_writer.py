import tkinter as tk
from tkinter import filedialog

class FileWriter:
    """Class for writing Bibtex files
    """
    def __init__(self) -> None:
        """Create filewriter instance
        """
        self._root = tk.Tk()
        self._root.withdraw()

    def _get_user_directory(self):
        directory = filedialog.askdirectory(title="Select Folder")
        return directory

    def write_bibtex(self):
        folder_path = self._get_user_directory()
        print(folder_path)

if __name__ == "__main__":
    f = FileWriter()
    f.write_bibtex()