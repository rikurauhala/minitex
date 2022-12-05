import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class FileWriter:
    """Class for writing Bibtex files
    """
    def __init__(self, folder_path: str = None) -> None:
        """Create filewriter instance
        """
        self._root = tk.Tk()
        self._root.withdraw()
        self._file_name = "references.bib"

        if folder_path:
            self._folder_path = Path(folder_path)
        else:
            self._folder_path = None

    def _get_user_directory(self) -> Path:
        """Prompt user for directory where to save the Bibtex file

        Returns:
            Path: path to directory
        """
        directory = filedialog.askdirectory(title="Select Folder")
        return Path(directory)

    def _make_entry_string(self, ref: dict) -> str:
        """Create entry string from reference to be saved in Bibtex file

        Return:
            str: entry to save in the file
        """
        if 'type' not in ref:
            ref_type = "@BOOK"
        else: ref_type = ref['type']

        return f"""{ref_type}{"{"}{ref['key']},
    title = "{ref['title']}",
    author = "{ref['authors']}",
    publisher = "{ref['publisher']}",
    year = "{ref['year']}"
{"}"}
"""

    def write_bibtex(self, references: list) -> None:
        """Write given list of reference objects to a Bibtex file
        """
        if not self._folder_path:
            self._folder_path = self._get_user_directory()

        file_path = self._folder_path.joinpath(self._file_name)

        try:
            with open(file_path, "a", encoding="utf-8") as file:
                for ref in references:
                    entry = self._make_entry_string(ref)

                    file.write("\n")
                    file.write(entry)

        except OSError:
            raise TypeError("Expected directory to be a valid path, instead got: ", file_path)
