import unittest
from utils.file_writer import FileWriter

class TestFileWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.test_writer = FileWriter(folder_path="./src/tests")
        self.test_entries = [{
                'key': 'Martin91',
                'authors': 'Martin, Robert',
                'title': 'Cognitive apprenticeship: making thinking visible',
                'year': '1991',
                'publisher': 'Prentice Hall'
            },
            {
                'key': 'TTT01',
                'authors': 'Testi, Testi and Testi, Tosto and Testo, Timo',
                'title': 'Testaillaan uudelleen',
                'year': '2001',
                'publisher': 'Kalevin koodilabra'
            }]

    def testIncorrectDirectory(self):
        with self.assertRaises(TypeError):
            f = FileWriter(folder_path=123)
        
        with self.assertRaises(TypeError):
            f = FileWriter(folder_path="123")
            f.write_bibtex()
