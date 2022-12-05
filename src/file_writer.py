from pathlib import Path


class FileWriter:
    """Class for writing Bibtex files
    """

    def __init__(self, folder_path: str = None) -> None:
        """Create filewriter instance
        """
        if folder_path is None:
            self._folder_path = Path("./data")
        else:
            self._folder_path = Path(folder_path)

        self._file_name = "references.bib"

    def get_filepath(self) -> str:
        """Get the filepath as an absolute path to the references.bib

        Return:
            str: get the filepath as a string
        """
        return str(self._folder_path.joinpath(self._file_name).resolve())

    def _make_entry_string(self, ref: dict) -> str:
        """Create entry string from reference to be saved in Bibtex file

        Return:
            str: entry to save in the file
        """
        if 'type' not in ref:
            ref_type = "@BOOK"
        else:
            ref_type = ref['type']

        return f"""{ref_type}{"{"}{ref['key']},
    title = "{ref['title']}",
    author = "{ref['authors']}",
    publisher = "{ref['publisher']}",
    year = "{ref['year']}"
{"}"}
"""

    def write_bibtex(self, references: list) -> bool:
        """Write given list of reference objects to a Bibtex file
        """
        file_path = self._folder_path.joinpath(self._file_name)

        try:
            with open(file_path, "a", encoding="utf-8") as file:
                file.truncate(0)
                for ref in references:
                    entry = self._make_entry_string(ref.data)
                    file.write("\n")
                    file.write(entry)
                return True

        except OSError as exc:
            raise TypeError('Expected directory to be a valid path, instead got: ',
                            file_path) from exc
