class Print():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ h ] print all the commands"

    def run(self):
        return self.app.print_commands()


class Add():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ n ] add a new reference"

    def run(self):
        return self.app.add_reference()


class AddDoi():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ o ] add a new reference based based on DOI"

    def run(self):
        return self.app.add_reference_from_doi()


class Show():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ s ] show all references"

    def run(self):
        return self.app.show_references()


class Export():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ e ] export the references to a BibTeX file"

    def run(self):
        return self.app.export_references()


class Delete():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ d ] delete a reference"

    def run(self):
        return self.app.delete_reference()


class Quit():
    def __str__(self):
        return "[ q ] quit"

class Edit():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ u ] edit a reference"

    def run(self):
        return self.app.edit_reference()
