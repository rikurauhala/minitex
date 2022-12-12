from os import name, system

from utils.commands import Print, Add, AddDoi, Show, Export, Delete, Quit, Edit
from services.reference_service import ReferenceService
from file_writer import FileWriter


class Application:
    """The main application."""

    def __init__(self, io, clear_at_start=None):
        """Initializes a new instance of the application."""
        self._commands = {
            "q": Quit(),
            "h": Print(self),
            "n": Add(self),
            "o": AddDoi(self),
            "s": Show(self),
            "e": Export(self),
            "d": Delete(self),
            "u": Edit(self)
        }
        self._IO = io
        self._reference_service = ReferenceService()
        self._file_writer = FileWriter()
        self._clear_at_start = True
        if clear_at_start == False:
            self._clear_at_start = False

    def start(self):
        """Starts the main application loop."""

        """Clears terminal at start if no False is given at app constructor 
            (to make robot framework tests show everything)"""
        if self._clear_at_start == True:
            self.clear_console()
        self.print_commands()
        while True:
            command = self._commands.get(self._IO.get_command())
            if not isinstance(command, Quit):
                if command:
                    command.run()
                else:
                    self._IO.print("Invalid command!")
            else:
                break

    def print_commands(self):
        """Prints a list of available commands."""
        self._IO.print("Commands:")
        for command in self._commands.values():
            self._IO.print(command)

    def add_reference(self):
        """Adds a new reference."""
        reference = self._IO.get_reference()
        self._reference_service.add_reference(reference)
        self._IO.print("Added a new reference.")

    def add_reference_from_doi(self):
        """Adds a new reference from DOI."""
        reference = self._IO.get_reference_from_doi()
        self._reference_service.add_reference(reference)
        self._IO.print("Added a new reference.")

    def export_references(self):
        """Exports the references to BibTeX."""
        if (self._file_writer.write_bibtex(self._reference_service.get_references())):
            self._IO.print("References exported to " +
                           self._file_writer.get_filepath() + " succesfully.")

    def show_references(self):
        """Prints all the references to the interface."""
        index = 1
        references = self._reference_service.get_references()
        if references:
            self._IO.print("References: ")
            for reference in references:
                self._IO.print(f"{index}: {reference}")
                index += 1
        else:
            self._IO.print("References have not been added yet.")

    def delete_reference(self):
        """Deletes a single reference."""
        id = self._IO.input_check_int(
            "Enter the index of the reference you wish to delete (q to cancel): ")
        references = self._reference_service.get_references()
        if id:
            id = int(id)
            if not id or len(references) < id:
                self._IO.print("Not a valid index.")
            else:
                self._reference_service.delete_reference(references[id - 1])
                self._IO.print("Reference deleted.")

    def edit_reference(self):
        """Edits a reference."""
        id = self._IO.input_check_int(
            "Enter the index of the reference you wish to edit (q to cancel): "
        )
        references = self._reference_service.get_references()
        if id:
            id = int(id)
            if not id or len(references) < id:
                self._IO.print("Not a valid index.")
            else:
                message = "Enter 1 to edit authors, 2 to edit title, 3 to edit year or 4 to edit publisher: "
                while True:
                    column = self._IO.input_check_int(message)
                    if int(column) >= 1 and int(column) <= 4:
                        break
                    else:
                        self._IO.print("Invalid input.")
                new_value = self._IO.input("Enter a new value: ")
                self._reference_service.edit_reference(new_value, id, int(column))
                self._IO.print("Reference edited.")

    def clear_console(self):
        """Clears the console."""
        if name == "nt":
            system("cls")
        else:
            system("clear")
