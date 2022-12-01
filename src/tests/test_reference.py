import unittest

from reference import Reference


class TestReference(unittest.TestCase):
    def setUp(self) -> None:
        author = "Martin, Robert"
        title = "Cognitive apprenticeship: making thinking visible"
        year = "1991"
        publisher = "Prentice Hall"
        self.r = Reference(author, title, year, publisher)

    def testInvalidAttributeValues(self):
        with self.assertRaises(TypeError):
            Reference(123, "title", "year", "publ")

        with self.assertRaises(ValueError):
            Reference("", "title", "year", "publ")

        with self.assertRaises(TypeError):
            Reference("author", "title", "year", None)

        with self.assertRaises(TypeError):
            self.r.title = 999
        
        with self.assertRaises(ValueError):
            self.r.year = ""

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
        ref = Reference(author, "test", "2011", "test")
        expected_key = "VPL11"
        key = ref.data["key"]

        assert isinstance(key, str)
        self.assertEqual(key, expected_key)

        author = "Allan Collins and John Seely Brown and Ann Holum"
        ref = Reference(author, "test", "1991", "test")
        expected_key = "CBH91"
        key = ref.data["key"]

        assert isinstance(key, str)
        self.assertEqual(key, expected_key)

    def testStrRepresentationIsCorrect(self):
        actual_string = self.r.__str__()
        expected_string = "Robert Martin | Cognitive apprenticeship: making thinking visible | Prentice Hall (1991)"
        self.assertEqual(actual_string, expected_string)

        author = "Obi-wan Kenobi and Anakin Skywalker and Yoda"
        reference = Reference(author, "Highground", "2005", "Lucasfilms")
        actual_string = reference.__str__()
        expected_string = "Obi-wan Kenobi, Anakin Skywalker and Yoda | Highground | Lucasfilms (2005)"
        self.assertEqual(actual_string, expected_string)
