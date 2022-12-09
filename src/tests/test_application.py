import unittest

from app import Application


class IOStub:
    def __init__(self):
        self.command = []
        self.reference = {
            "authors": "Doe, John and Caesar, Julius",
            "title": "Very good title",
            "year": "1999",
            "publisher": "Otava"
        }
        self.printitems = []
        self.indx = 1

    def get_command(self):
        print(self.command)
        return self.command.pop(0)

    def give_command(self, command):
        self.command.append(command)

    def get_reference(self):
        return self.reference

    def print(self, item):
        self.printitems.append(item)
    
    def input_check_int(self, message):
        return self.indx


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.IO = IOStub()
        self.app = Application(self.IO)

    def test_prints_commands(self):
        self.app._IO.give_command("h")
        self.app._IO.give_command("q")
        self.app.start()
        command = self.app._IO.printitems[10]
        self.assertEqual(str(command), "[ q ] quit")

    def test_adds_reference(self):
        self.app._IO.give_command("n")
        self.app._IO.give_command("d")
        self.app._IO.give_command("q")
        self.app.start()
        message = self.app._IO.printitems[9]
        self.assertEqual(message, "Added a new reference.")

    def test_prints_references(self):
        self.app._IO.give_command("n")
        self.app._IO.give_command("s")
        self.app._IO.give_command("d")
        self.app._IO.give_command("q")
        self.app.start()
        reference = self.app._IO.printitems[11]
        self.assertIn("John Doe", reference)
        self.assertIn("Julius Caesar", reference)

    def test_invalid_command(self):
        self.app._IO.give_command("x")
        self.app._IO.give_command("d")
        self.app._IO.give_command("q")
        self.app.start()
        message = self.app._IO.printitems[9]
        self.assertEqual(message, "Invalid command!")
