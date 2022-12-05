import os.path
import unittest
import tempfile
from entities.reference import Reference

from file_writer import FileWriter

class TestFileWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.folder_path = "./src/tests"
        self.test_entries = [Reference('Martin, Robert', 'Cognitive apprenticeship: making thinking visible',
        '1991', 'Prentice Hall'), Reference('Testi, Testi and Testi, Tosto and Testo, Timo', 'Testaillaan uudelleen',
                '2001', 'Kalevin koodilabra')]

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
                content = references.read(16)
                expected_content = "\n@BOOK{Martin91,"

                self.assertEqual(content, expected_content)
                self.assertEqual(len(references.read()), 321)