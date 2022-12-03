import unittest

from entities.reference import Reference
from repositories.reference_repository import reference_repository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = reference_repository
        self.reference1 = Reference(
            author="Kenobi, Obi-wan",
            title="It's over Anakin, I have the high ground!",
            year="2005",
            publisher="George Lucas"
        )
        self.reference2 = Reference(
            author="Ki-Adi-Mundi",
            title="What About the Droid Attack on the Wookiees?",
            year="2005",
            publisher="George Lucas"
        )
    
    """ Disabled until there is a test database
    def test_creates_item_to_repository(self):
        self.repository.create(self.reference1)
        references = self.repository.find_all()
        self.assertEqual(len(references), 1)

    def test_creates_multiple_items_to_repository(self):
        self.repository.create(self.reference1)
        self.repository.create(self.reference2)
        references = self.repository.find_all()
        self.assertEqual(len(references), 2)

    def test_returns_items_from_repository(self):
        self.repository.create(self.reference1)
        self.repository.create(self.reference2)
        items = self.repository.find_all()
        self.assertEqual(items[0], self.reference1)
        self.assertEqual(items[1], self.reference2)
    """
