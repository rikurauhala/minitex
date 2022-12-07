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

    def test_creates_item_to_repository(self):
        self.repository.create(self.reference1)
        references = self.repository.find_all()
        self.assertEqual(len(references.fetchall()), 1)
        self.repository.delete(self.reference1)

    def test_creates_multiple_items_to_repository(self):
        self.repository.create(self.reference1)
        self.repository.create(self.reference2)
        references = self.repository.find_all()
        self.assertEqual(len(references.fetchall()), 2)
        self.repository.delete(self.reference1)
        self.repository.delete(self.reference2)

    def test_returns_items_from_repository(self):
        self.repository.create(self.reference1)
        self.repository.create(self.reference2)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], self.reference1.author)
        self.assertEqual(items[1][1], self.reference2.author)
        self.repository.delete(self.reference1)
        self.repository.delete(self.reference2)
