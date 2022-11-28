import unittest
from reference import Reference

class TestReference(unittest.TestCase):
	def setUp(self) -> None:
		author = "Martin, Robert"
		title = "Cognitive apprenticeship: making thinking visible"
		year = "1991"
		publisher = "Prentice Hall"
		
		self.r = Reference(author, title , year, publisher)

	def testInvalidAuthorValue(self):
		a = 123
		t = "Abcd"
		y = "1992"
		p = "Kalevi"

		with self.assertRaises(TypeError):
			r = Reference(a, t, y, p)

		with self.assertRaises(ValueError):
			r = Reference("", t, y, p)

		with self.assertRaises(TypeError):
			self.r.author = 999

		with self.assertRaises(ValueError):
			self.r.author = ""

	def testPropertiesReturnsCorrectValues(self):
		assert isinstance(self.r.author, str)
		assert isinstance(self.r.title, str)
		assert isinstance(self.r.year, str)
		assert isinstance(self.r.publisher, str)

	def testDataPropertyReturnsDict(self):
		excepted_data = {
			'key': 'Martin91', 
			'authors': 'Martin, Robert', 
			'title': 'Cognitive apprenticeship: making thinking visible', 
			'year': '1991', 
			'publisher': 'Prentice Hall'
		}

		assert isinstance(self.r.data, dict)
		self.assertEqual(self.r.data, excepted_data)
	
	def testGenKeyGeneratesCorrectKeys(self):
		author = "Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti"
		ref = Reference(author, "", "2011", "")
		expected_key = "VPL11"
		key = ref.data["key"]

		assert isinstance(key, str)
		self.assertEqual(key, expected_key)


		author = "Allan Collins and John Seely Brown and Ann Holum"
		ref = Reference(author, "", "1991", "")
		expected_key = "CBH91"
		key = ref.data["key"]

		assert isinstance(key, str)
		self.assertEqual(key, expected_key)