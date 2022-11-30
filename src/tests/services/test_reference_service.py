import unittest
from services.reference_service import ReferenceService

class TestReferenceRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = ReferenceService()
    
    def test_adds_one_reference(self):
        reference = {"authors":"Doe, John and Caesar, Julius","title": "Very good title","year": "1999","publisher": "Otava"}
        self.repository.add_reference(reference)
        storedref = self.repository.get_references()[0]
        self.assertEqual(storedref.author, "Doe, John and Caesar, Julius")
        self.assertEqual(storedref.title, "Very good title")
        self.assertEqual(storedref.year, "1999")
        self.assertEqual(storedref.publisher, "Otava")

    def test_adds_multiple_references(self):
        reference1 = {"authors":"Doe, John and Caesar, Julius","title": "Very good title","year": "1999","publisher": "Otava"}
        reference2 = {"authors":"Dracul, Vlad and Caesar, Julius","title": "Super good title","year": "2001","publisher": "Kodansha"}
        self.repository.add_reference(reference1)
        self.repository.add_reference(reference2)
        storedref1, storedref2 = self.repository.get_references()[0], self.repository.get_references()[1]
        self.assertEqual(storedref1.author, "Doe, John and Caesar, Julius")
        self.assertEqual(storedref1.title, "Very good title")
        self.assertEqual(storedref1.year, "1999")
        self.assertEqual(storedref1.publisher, "Otava")
        self.assertEqual(storedref2.author, "Dracul, Vlad and Caesar, Julius")
        self.assertEqual(storedref2.title, "Super good title")
        self.assertEqual(storedref2.year, "2001")
        self.assertEqual(storedref2.publisher, "Kodansha")
