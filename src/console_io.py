import crossref_commons.retrieval as ccr
from colorama import Fore, Style


class ConsoleIO:
    """Module for user input and output."""

    def print(self, string):
        """Prints a given string to the console.

        Args:
            string: The string to be printed.
        """
        print(string)

    def print_valid(self, string):
        """Prints a given string to the console in a green color.

        Args:
            string: The string to be printed.
        """
        print(f'{Fore.GREEN}' + string + f'{Style.RESET_ALL}')

    def print_invalid(self, string):
        """Prints a given string to the console in a red color.

        Args:
            string: The string to be printed.
        """
        print(f'{Fore.RED}' + string + f'{Style.RESET_ALL}')

    def input(self, string):
        """Asks for a input and check if it's empty, if empty asks again.

        Returns:
            string: Input as a string.
        """
        while True:
            enter = input(string)
            if enter:
                return enter
            self.print_invalid("Input can not be empty, try again.")

    def input_check_int(self, string):
        """Asks for a input and check if it's an integer.

        Returns:
            int: input as an integer
        """
        while True:
            integer = input(string)
            if integer.isnumeric():
                return integer
            self.print_invalid("Input must be an integer, try again.")

    def get_command(self):
        """Asks for a command from the user.

        Returns:
            str: Lowercase command as a string.
        """
        return input("Input command: ").lower()

    def input_authors(self):
        """Asks for multiple authors from the user.

        Returns:
            string: authors as a string combined with and in between
        """
        authors = ""
        while True:
            author = self.input(
                "Input authors in format lastname, firstname (q to stop): ")
            if author.lower() == "q":
                if authors:
                    break
                self.print("At least one author is required.")
            elif author and authors:
                authors += " and " + author
            elif author:
                authors += author
        return authors

    def get_reference(self):
        """Asks for a reference from the user.

        Returns:
            dict: authors, title, year published and publisher as dict.
        """
        authors = self.input_authors()
        title = self.input("Input title: ")
        year = self.input_check_int("Input year published: ")
        publisher = self.input("Input publisher: ")
        reference = {
            "authors": authors,
            "title": title,
            "year": year,
            "publisher": publisher
        }
        return reference

    def get_reference_from_doi(self):
        """Asks for a DOI from the user.

        Returns:
            dict: authors, title, year published and publisher as dict.
        """
        while True:
            try:
                doi = input("Insert a valid DOI: ")
                reference = ccr.get_publication_as_json(doi)
            except ValueError:
                self.print("Invalid DOI. Try again.")
                continue
            reference_type = reference["type"]
            if reference_type != "book":
                self.print("Reference must be a book. Try again.")
                continue
            year = reference["published-online"]["date-parts"][0][0]
            editors = reference["editor"]
            authors_list = []
            for author in editors:
                first = author["given"]
                last = author["family"]
                authors_list.append(f"{first} {last}")
            authors = " and ".join(authors_list)
            title = reference["title"][0]
            publisher = reference["publisher"]
            reference = {
                "authors": authors,
                "title": title,
                "year": str(year),
                "publisher": publisher
            }
            return reference
