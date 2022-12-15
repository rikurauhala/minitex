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
            if isinstance(command, Quit):
                break
            if command:
                command.run()
            else:
                self._IO.print_invalid("Invalid command!")

    def print_commands(self):
        """Prints a list of available commands."""
        self._IO.print("Commands:")
        for command in self._commands.values():
            self._IO.print(command)

    def add_reference(self):
        """Adds a new reference."""
        reference = self._IO.get_reference()
        if self._reference_service.add_reference(reference):
            self._IO.print_valid("Added a new reference.")
        else:
            self._IO.print_invalid("You have added this reference already.")

    def add_reference_from_doi(self):
        """Adds a new reference from DOI."""
        if reference := self._IO.get_reference_from_doi():
            if self._reference_sgervice.add_reference(reference):
                self._IO.print_valid("Added a new reference.")
            else:
                self._IO.print_invalid("You have added this reference already.")
        else:
            self._IO.print_invalid("Something went wrong, make sure you are connected to internet.")

    def export_references(self):
        """Exports the references to BibTeX."""
        if (self._file_writer.write_bibtex(self._reference_service.get_references())):
            self._IO.print_valid("References exported to " +
                                 self._file_writer.get_filepath() + " succesfully.")

    def show_references(self):
        """Prints all the references to the interface."""
        if references := self._reference_service.get_references():
            self._IO.print("References: ")
            for index, reference in enumerate(references, start=1):
                self._IO.print(f"{index}: {reference}")
        else:
            self._IO.print("References have not been added yet.")

    def delete_reference(self):
        """Deletes a single reference."""
        index = self._IO.input_check_int(
            "Enter the index of the reference you wish to delete: ")
        if reference := self._reference_service.get_reference(int(index) - 1):
            self._reference_service.delete_reference(reference)
            self._IO.print_valid("Reference deleted.")
        else:
            self._IO.print_invalid("Not a valid index.")

    def edit_reference(self):
        """Edits a reference."""
        if not (id := self._IO.input_check_int("Enter the index of the reference you wish to edit: ")):
            return
        if reference := self._reference_service.get_reference(int(id) - 1):
            message = "[ 1 ] edit authors\n[ 2 ] edit title\n[ 3 ] edit year\n[ 4 ] edit publisher"
            while True:
                self._IO.print(message)
                column = int(self._IO.input_check_int(
                    "Input field to edit: "))
                if column and 4 >= column >= 1:
                    break
                else:
                    self._IO.print_invalid(
                        "Invalid input, try again.")
            if column == 1:
                new_value = self._IO.input_authors()
            elif column == 3:
                new_value = self._IO.input_check_int("Enter a new value: ")
            else:
                new_value = self._IO.input("Enter a new value: ")
            self._reference_service.edit_reference(
                reference, column, new_value)
            self._IO.print_valid("Reference edited.")
        else:
            self._IO.print_invalid("Not a valid index.")

    def clear_console(self):
        """Clears the console."""
        if name == "nt":
            system("cls")
        else:
            system("clear")
