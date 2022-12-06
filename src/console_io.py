class ConsoleIO:
    """Module for user input."""

    def print(self, string):
        print(string)

    def input(self, string):
        """Asks for a input and check if it's empty, if empty ask again

        Returns:
            string: input as a string
        """
        while True:
            enter = input(string)
            if enter:
                return enter
            self.print("Input can not be empty.")

    def input_int(self, string):
        """Asks for a input and check if it's int

        Returns:
            int: input as an integer
        """
        while True:
            integer = input(string)
            if integer.isnumeric():
                return int(integer)
            if integer == "q":
                break
            self.print("Input must be an integer. ")

    def get_command(self):
        """Asks command from the user

        Returns:
            str: lower case command as str
        """
        return input("Input command: ").lower()

    def get_reference(self):
        """Asks reference from the user

        Returns:
            dict: authors, title, year published and publisher as dict
        """
        authors = ""
        while True:
            author = self.input(
                "Input authors in format lastname, firstname (q to stop): ")
            if author.lower() == "q":
                if authors:
                    break
                self.print("Atleast one author is required.")
            elif author and authors:
                authors += " and " + author
            elif author:
                authors += author
        title = self.input("Input title: ")
        year = self.input_int("Input year published: ")
        publisher = self.input("Input publisher: ")
        return {"authors": authors, "title": title, "year": str(year), "publisher": publisher}
