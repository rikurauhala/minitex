class ConsoleIO:
    """Module for user input."""

    def print(self, string):
        """Prints the given string"""
        print(string)

    def input(self, string):
        return input(string)

    def input_int(self, string):
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
            author = input("Input author in format lastname, firstname or input q to stop: ")
            if author == "q":
                if len(authors) > 0:
                    break
                print("At least one author is required")
            elif author and authors:
                authors += " and " + author
            elif author:
                authors += author
        title = self.input("Input title: ")
        year = self.input_int("Input year published: ")
        publisher = self.input("Input publisher: ")
        if authors and title and year and publisher:
            return {"authors": authors, "title": title, "year": str(year), "publisher": publisher}
        self.print("Something went wrong, did you fill all the fields?")
