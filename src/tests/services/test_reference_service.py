import unittest

from services.reference_service import ReferenceService
from repositories.database import Repository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        self.repository = ReferenceService()
        self.database = Repository()
        self.database.drop_tables()
        self.database.create_table()
        self.reference1 = {
            "authors": "Doe, John and Caesar, Julius",
            "title": "Very good title",
            "year": "1999",
            "publisher": "Otava"
        }
        self.reference2 = {
            "authors": "Dracul, Vlad and Caesar, Julius",
            "title": "Super good title",
            "year": "2001",
            "publisher": "Kodansha"
        }
    
    def test_adds_one_reference(self):
        self.repository.add_reference(self.reference1)
        stored_ref = self.repository.get_references()[0]
        self.assertEqual(stored_ref.author, self.reference1["authors"])
        self.assertEqual(stored_ref.title, self.reference1["title"])
        self.assertEqual(stored_ref.year, self.reference1["year"])
        self.assertEqual(stored_ref.publisher, self.reference1["publisher"])

    def test_adds_multiple_references(self):
        self.repository.add_reference(self.reference1)
        self.repository.add_reference(self.reference2)
        stored_ref1 = self.repository.get_references()[0]
        stored_ref2 = self.repository.get_references()[1]
        self.assertEqual(stored_ref1.author, self.reference1["authors"])
        self.assertEqual(stored_ref1.title, self.reference1["title"])
        self.assertEqual(stored_ref1.year, self.reference1["year"])
        self.assertEqual(stored_ref1.publisher, self.reference1["publisher"])
        self.assertEqual(stored_ref2.author, self.reference2["authors"])
        self.assertEqual(stored_ref2.title, self.reference2["title"])
        self.assertEqual(stored_ref2.year, self.reference2["year"])
        self.assertEqual(stored_ref2.publisher, self.reference2["publisher"])
