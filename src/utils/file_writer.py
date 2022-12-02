import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class FileWriter:
    """Class for writing Bibtex files
    """
    def __init__(self) -> None:
        """Create filewriter instance
        """
        self._root = tk.Tk()
        self._root.withdraw()
        self._FILENAME = "references.bib"

    def _get_user_directory(self) -> Path:
        """Prompt user for directory where to save the Bibtex file

        Returns:
            str: path to directory
        """
        directory = filedialog.askdirectory(title="Select Folder")
        return Path(directory)

    def write_bibtex(self):
        folder_path = self._get_user_directory()
        file_path = folder_path.joinpath(self._FILENAME)

        print(file_path.is_file())

if __name__ == "__main__":
    f = FileWriter()
    f.write_bibtex()