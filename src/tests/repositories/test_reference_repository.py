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
        self.repository.delete_all()

    def test_returns_items_from_repository(self):
        self.repository.create(self.reference1)
        self.repository.create(self.reference2)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], self.reference1.author)
        self.assertEqual(items[1][1], self.reference2.author)
        self.repository.delete_all()

    def test_edit_author(self):
        self.repository.create(self.reference1)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], self.reference1.author)
        new_author = "New author"
        self.repository.edit(self.reference1, 1, new_author)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], new_author)
        self.repository.delete_all()

    def test_edit_title(self):
        self.repository.create(self.reference1)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], self.reference1.author)
        new_title = "New title"
        self.repository.edit(self.reference1, 2, new_title)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][2], new_title)
        self.repository.delete_all()

    def test_edit_year(self):
        self.repository.create(self.reference1)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], self.reference1.author)
        new_year = 2005
        self.repository.edit(self.reference1, 3, new_year)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][3], new_year)
        self.repository.delete_all()

    def test_edit_publisher(self):
        self.repository.create(self.reference1)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][1], self.reference1.author)
        new_publisher = "New publisher"
        self.repository.edit(self.reference1, 4, new_publisher)
        items = self.repository.find_all().fetchall()
        self.assertEqual(items[0][4], new_publisher)
        self.repository.delete_all()
