import unittest

from console_io import ConsoleIO


class StubIO(ConsoleIO):
    def __init__(self):
        self.first = True

    def input(self, message):
        if self.first:
            self.first = False
            return "10.1002/9780470209943"
        return "q"


class TestConsoleIO(unittest.TestCase):
    def setUp(self):
        self.IO = StubIO()
        self.reference = self.IO.get_reference_from_doi()
        self.doi = {
            "authors": "Abbie Griffin and Stephen Somermeyer",
            "title": "The PDMA ToolBook 3 for New Product Development",
            "year": "2007",
            "publisher": "John Wiley & Sons, Inc."
        }

    def test_adding_valid_doi_adds_returns_book_reference(self):
        self.assertEqual(self.doi, self.reference)

    def test__doi_returns_the_correct_authors(self):
        self.assertEqual(self.reference.get("authors"),
                         self.doi.get("authors"))

    def test__doi_returns_the_correct_title(self):
        self.assertEqual(self.reference.get("title"),
                         self.doi.get("title"))

    def test__doi_returns_the_correct_year(self):
        self.assertEqual(self.reference.get("year"),
                         self.doi.get("year"))

    def test__doi_returns_the_correct_publisher(self):
        self.assertEqual(self.reference.get("publisher"),
                         self.doi.get("publisher"))
