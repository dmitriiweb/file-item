from pathlib import Path
import unittest

from file_item import File


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_basedir(self):
        basedir = File.basedir(__file__)
        self.assertEqual(basedir, Path(__file__).parent)

    def test_repr(self):
        file = File('test.csv', '/home/user/test.csv')
        self.assertEqual(repr(file), 'File(name="test.csv", path="/home/user/test.csv")')

    def test_repr_path_none(self):
        file = File('test.csv')
        self.assertEqual(repr(file), 'File(name="test.csv", path="./test.csv")')
