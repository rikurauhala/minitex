import unittest
from repositories.reference_repository import ReferenceRepository

class TestReferenceRepository(unittest.TestCase):
    def setUp(self) -> None:
	    self.repository = ReferenceRepository()
    