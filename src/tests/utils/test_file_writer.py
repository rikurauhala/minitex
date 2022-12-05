import os.path
import unittest
import tempfile

from utils.file_writer import FileWriter

class TestFileWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.folder_path = "./src/tests"
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

    def testWriteBibtexWritesToFile(self):
        with tempfile.TemporaryDirectory(dir=self.folder_path) as tmp_dir:
            self.test_writer = FileWriter(tmp_dir)
            self.test_writer.write_bibtex(self.test_entries)

            self.assertTrue(os.path.isdir(tmp_dir))

            with open(tmp_dir + "/references.bib", "r") as references:
                content = references.read(6)
                expected_content = "\n@BOOK"
                self.assertEqual(content, expected_content)
