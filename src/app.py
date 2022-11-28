from os import name, system

from utils.commands import COMMANDS


class Application:
    """The main application."""

    def __init__(self, io):
        """Initializes a new instance of the application."""
        self._commands = COMMANDS
        self._IO = io

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
                case _:
                    self._print_invalid_command()

    def _print_commands(self):
        """Prints a list of available commands."""
        print("Commands:")
        for command in self._commands.items():
            print(command[1])

    def _print_invalid_command(self):
        """Prints a message signifying an invalid command."""
        print("Invalid command!")

    def _clear_console(self):
        """Clears the console."""
        if name == "nt":
            system("cls")
        else:
            system("clear")
