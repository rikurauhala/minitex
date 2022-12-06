class StubIO:
    """Module for simulating user input."""

    def __init__(self, inputs = None):
        """Creates list for inputs that gets string inputs resource.robot arguments
            Creates list for outputs that StubIO fills and robot framework test environment reads"""
        self.inputs = inputs or []
        self.outputs = []

    def print(self, output):
        """Adds prompt from app into ouputs list"""
        self.outputs.append(output)

    def get_command(self):
        """Takes preset command from inputs list when app asks for it"""
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def give_command(self, input):
        """Robot Framework uses AppLibrary (which uses this method) to fill command inputs with resource.robot 
            arguments before the app starts"""
        self.inputs.append(input)

    def get_reference(self):
        """Gets information for reference (that robot test file put there in arguments) from the inputs list

        Returns:
            dict: authors, title, year published and publisher as dict
        """

        authors = ""
        while True:
            author = self.inputs.pop(0)
            if author == "q":
                if len(authors) > 0:
                    break
                print("At least one author is required")
            elif author and authors:
                authors += " and " + author
            elif author:
                authors += author
        title = self.inputs.pop(0)
        year = self.inputs.pop(0)
        publisher = self.inputs.pop(0)
        if authors and title and year and publisher:
            return {"authors": authors, "title": title, "year": str(year), "publisher": publisher}
        self.print("Something went wrong, did you fill all the fields?")