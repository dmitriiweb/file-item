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
