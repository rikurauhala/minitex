import unittest
from services.reference_service import ReferenceService

class TestReferenceRepository(unittest.TestCase):
    def setUp(self) -> None:
	    self.repository = ReferenceService()
    