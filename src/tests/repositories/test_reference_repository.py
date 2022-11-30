import unittest
from repositories.reference_repository import ReferenceRepository

class TestReferenceRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = ReferenceRepository()
    
    def test_adds_item_to_reposiotory(self):
        item = ["itemtoadd"]
        self.repository.add(item)
        self.assertEqual(self.repository.references[0], item)

    def test_adds_multiple_items_to_repository(self):
        item1 = ["item1toadd"]
        item2 = ["item2toadd"]
        self.repository.add(item1)
        self.repository.add(item2)
        self.assertEqual(self.repository.references[0], item1)
        self.assertEqual(self.repository.references[1], item2)

    def test_returns_items_from_repository(self):
        item1 = ["item1toadd"]
        item2 = ["item2toadd"]
        self.repository.add(item1)
        self.repository.add(item2)
        items = self.repository.find_all()
        self.assertEqual(items[0], item1)
        self.assertEqual(items[1], item2)
