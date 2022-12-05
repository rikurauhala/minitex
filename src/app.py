from os import name, system

from utils.commands import COMMANDS
from services.reference_service import ReferenceService
from file_writer import FileWriter

class Application:
    """The main application."""

    def __init__(self, io):
        """Initializes a new instance of the application."""
        self._commands = COMMANDS
        self._IO = io
        self._reference_service = ReferenceService()
        self._file_writer =FileWriter()

    def start(self):
        """Starts the main application loop."""

        self._clear_console()
        self._print_commands()

        while True:
            command = self._IO.get_command()
            match command:
                case 'q':
                    break
                case 'h':
                    self._print_commands()
                case "n":
                    reference = self._IO.get_reference()
                    if reference:
                        self._reference_service.add_reference(reference)
                        self._IO.print("Added a new reference.")
                case 's':
                    self._IO.print("References: ")
                    index = 1
                    for reference in self._reference_service.get_references():
                        self._IO.print(f"{index}: {reference}")
                        index += 1
                case 'e':
                    self._file_writer.write_bibtex(self._reference_service.get_references())
                case _:
                    self._print_invalid_command()

    def _print_commands(self):
        """Prints a list of available commands."""
        self._IO.print("Commands:")
        for command in self._commands.items():
            self._IO.print(command[1])

    def _print_invalid_command(self):
        """Prints a message signifying an invalid command."""
        self._IO.print("Invalid command!")

    def _clear_console(self):
        """Clears the console."""
        if name == "nt":
            system("cls")
        else:
            system("clear")
