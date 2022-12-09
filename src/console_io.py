import crossref_commons.retrieval as ccr


class ConsoleIO:
    """Module for user input and output."""

    def print(self, string):
        """Prints a given string to the console.

        Args:
            string: The string to be printed.
        """
        print(string)

    def input(self, string):
        """Asks for a input and check if it's empty, if empty asks again.

        Returns:
            string: Input as a string.
        """
        while True:
            enter = input(string)
            if enter:
                return enter
            self.print("Input can not be empty, try again.")

    def input_check_int(self, string):
        """Asks for a input and check if it's an integer.

        Returns:
            int: input as an integer
        """
        while True:
            integer = input(string)
            if integer.isnumeric():
                return integer
            if integer == "q":
                break
            self.print("Input must be an integer, try again.")

    def get_command(self):
        """Asks for a command from the user.

        Returns:
            str: Lowercase command as a string.
        """
        return input("Input command: ").lower()

    def get_reference(self):
        """Asks for a reference from the user.

        Returns:
            dict: authors, title, year published and publisher as dict.
        """
        authors = ""
        while True:
            author = self.input("Input authors in format lastname, firstname (q to stop): ")
            if author.lower() == "q":
                if authors:
                    break
                self.print("At least one author is required.")
            elif author and authors:
                authors += " and " + author
            elif author:
                authors += author
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
        while True:
            try:
                doi = input("Insert a valid DOI: ")
                reference = ccr.get_publication_as_json(doi)
            except ValueError:
                self.print("Invalid DOI. Try again.")
                continue
            #type = reference["type"]
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
