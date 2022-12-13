import unittest

from console_io import ConsoleIO


class StubIO(ConsoleIO):
    def input(self, message):
        return "10.1002/9780470209943"


class TestConsoleIO(unittest.TestCase):
    def setUp(self):
        self.IO = StubIO()
        self.reference = self.IO.get_reference_from_doi()

    def test__doi_returns_the_correct_authors(self):
        self.assertEqual(self.reference.get("authors"),
                         "Abbie Griffin and Stephen Somermeyer")

    def test__doi_returns_the_correct_title(self):
        self.assertEqual(self.reference.get("title"),
                         "The PDMA ToolBook 3 for New Product Development")

    def test__doi_returns_the_correct_year(self):
        self.assertEqual(self.reference.get("year"), "2007")

    def test__doi_returns_the_correct_publisher(self):
        self.assertEqual(self.reference.get("publisher"),
                         "John Wiley & Sons, Inc.")
