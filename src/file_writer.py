from pathlib import Path


class FileWriter:
    """Class for writing Bibtex files."""

    def __init__(self, folder_path: str = None) -> None:
        """Creates a new instance of FileWriter.

        Args:
            folder_path (str, optional): Defaults to None.
        """
        if folder_path is None:
            self._folder_path = Path("./data")
        else:
            self._folder_path = Path(folder_path)

        self._file_name = "references.bib"

    def get_filepath(self) -> str:
        """Gets the filepath as an absolute path to the references.bib.

        Return:
            str: The filepath as a string.
        """
        return str(self._folder_path.joinpath(self._file_name).resolve())

    def _make_entry_string(self, ref: dict) -> str:
        """Creates an entry string from reference to be saved into a Bibtex file.

        Return:
            str: Entry to save into the file
        """
        ref_type = "@BOOK" if "type" not in ref else ref["type"]
        return f"""{ref_type}{"{"}{ref['key']},
    title = "{ref['title']}",
    author = "{ref['authors']}",
    publisher = "{ref['publisher']}",
    year = "{ref['year']}"
{"}"}
"""

    def write_bibtex(self, references: list) -> bool:
        """Writes a given list of reference objects into a Bibtex file."""
        file_path = self._folder_path.joinpath(self._file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.truncate(0)
                for ref in references:
                    entry = self._make_entry_string(ref.data)
                    file.write("\n")
                    file.write(entry)
                return True

        except OSError as exc:
            raise TypeError(
                "Expected directory to be a valid path, instead got: ", file_path
            ) from exc
