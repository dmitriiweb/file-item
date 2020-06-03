from pathlib import Path
import unittest

from file_item import File


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = File('test.csv', '/home/user/test.csv')
        self.file_no_path = File('test.csv')
        pass

    def test_basedir(self):
        basedir = File.basedir(__file__)
        self.assertEqual(basedir, Path(__file__).parent)

    def test_repr(self):
        self.assertEqual(repr(self.file_path), 'File(name="test.csv", path="/home/user/test.csv")')

    def test_repr_path_none(self):
        self.assertEqual(repr(self.file_no_path), 'File(name="test.csv", path="./test.csv")')

    def test_str(self):
        self.assertEqual(str(self.file_path), '/home/user/test.csv')

    def test_str_path_none(self):
        self.assertEqual(str(self.file_no_path), './test.csv')

    def test_eq(self):
        file2 = File('test.csv', '/home/user/test.csv')
        self.assertTrue(self.file_path == file2)

    def test_no_eq(self):
        self.assertFalse(self.file_path ==  self.file_no_path)

    def test_wrong_class_eq(self):
        self.assertFalse(self.file_path == 2)
        
    def test_str_eq(self):
        self.assertTrue(self.file_path == self.file_path.path)
