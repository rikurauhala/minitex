class Print():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ h ] print all the commands"

    def run(self):
        return self.app._print_commands()


class Add():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ n ] add a new reference"

    def run(self):
        return self.app._add_reference()


class Show():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ s ] show all references"

    def run(self):
        return self.app._show_references()


class Export():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ e ] export the references to a BibTeX file"

    def run(self):
        return self.app._export_references()


class Delete():
    def __init__(self, app):
        self.app = app

    def __str__(self):
        return "[ d ] delete a reference"

    def run(self):
        return self.app._delete_reference()

class Quit():
    def __str__(self):
        return "[ q ] quit"
