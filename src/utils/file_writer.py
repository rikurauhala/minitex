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
            Path: path to directory
        """
        directory = filedialog.askdirectory(title="Select Folder")
        return Path(directory)

    def write_bibtex(self, references: list = None):
        folder_path = self._get_user_directory()
        file_path = folder_path.joinpath(self._FILENAME)

        with open(file_path, "a") as file:
            for ref in references:
                if 'type' not in ref:
                    ref_type = "@BOOK"
                else: ref_type = ref['type']

                entry = f"""{ref_type}{"{"}{ref['key']},
                    title = "{ref['title']}",
                    author = "{ref['authors']}",
                    publisher = "{ref['publisher']}",
                    year = "{ref['year']}",
                {"},"}
                """
                print(entry)
                file.write(entry)


if __name__ == "__main__":
    f = FileWriter()
    test = [{
            'key': 'Martin91', 
            'authors': 'Martin, Robert', 
            'title': 'Cognitive apprenticeship: making thinking visible', 
            'year': '1991', 
            'publisher': 'Prentice Hall'
        },
        {
            'key': 'TTT01', 
            'authors': 'Testi, Testi and Testi, Tosto and Testo, Timo', 
            'title': 'Testaillaan uudelleen', 
            'year': '2001', 
            'publisher': 'Kalevin koodilabra'
        }]
    f.write_bibtex(test)