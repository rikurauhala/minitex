import unittest
from app import Application

class IOStub:
    def __init__(self):
        self.command = []
        self.reference = {"authors":"Doe, John and Caesar, Julius","title": "Very good title","year": "1999","publisher": "Otava"}
        self.printitems = []

    def get_command(self):
        print(self.command)
        return self.command.pop(0)

    def give_command(self, comm):
        self.command.append(comm)

    def get_reference(self):
        return self.reference

    def print(self, item):
        self.printitems.append(item)

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.IO = IOStub()
        self.app = Application(self.IO)

    def test_prints_commands(self):
        self.app._IO.give_command("h")
        self.app._IO.give_command("q")
        self.app.start()

        command1 = self.app._IO.printitems[6]
        self.assertEqual(command1, "[ q ] quit")

    def test_adds_reference(self):
        self.app._IO.give_command("n")
        self.app._IO.give_command("q")
        self.app.start()
        message = self.app._IO.printitems[5]
        self.assertEqual(message, "Added a new reference.")

    def test_prints_references(self):
        self.app._IO.give_command("n")
        self.app._IO.give_command("s")
        self.app._IO.give_command("q")
        self.app.start()
        reference = self.app._IO.printitems[7]
        self.assertEqual(reference.author, "Doe, John and Caesar, Julius")

    def test_invalid_command(self):
        self.app._IO.give_command("x")
        self.app._IO.give_command("q")
        self.app.start()
        message = self.app._IO.printitems[5]
        self.assertEqual(message, "Invalid command!")
