from os import name, system

from utils.commands import Print, Add, Show, Export, Delete, Quit
from services.reference_service import ReferenceService
from file_writer import FileWriter


class Application:
    """The main application."""

    def __init__(self, io, clear_at_start=None):
        """Initializes a new instance of the application."""
        self._commands = {"q": Quit(), "h": Print(self), "n": Add(self), "s": Show(self),
                          "e": Export(self), "d": Delete(self)}
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
                    self.print_invalid_command()
            else:
                break

    def print_commands(self):
        """Prints a list of available commands."""
        self._IO.print("Commands:")
        for command in self._commands.values():
            self._IO.print(command)

    def print_invalid_command(self):
        """Prints a message signifying an invalid command."""
        self._IO.print("Invalid command!")

    def add_reference(self):
        """Adds a new reference."""
        reference = self._IO.get_reference()
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

    def clear_console(self):
        """Clears the console."""
        if name == "nt":
            system("cls")
        else:
            system("clear")
