class ConsoleIO:
    """Module for user input."""

    def get_command(self):
        """Asks command from the user

        Returns:
            str: lower case command as str
        """
        return input("Input command: ").lower()

    def get_reference(self):
        """Asks reference from the user

        Returns:
            list: authors, title, year published and publisher as list
        """

        authors = ""
        while True:
            author = input("Input author in format lastname, firstname or input q to stop: ")
            if author == "q":
                if len(authors) > 0:
                    authors = authors[0:-5]
                    break
                print("At least one author is required")
            else:
                authors += author + " and "
        title = input("Input title: ")
        year = input("Input year published: ")
        publisher = input("Input publisher: ")
        return [authors, title, year, publisher]
