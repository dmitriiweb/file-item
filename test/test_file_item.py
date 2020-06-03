from pathlib import Path
import unittest

from file_item import File

TEST_PATH = '/home/user/test.csv'
TEST_PATH2 = '/home/user/test2.csv'


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self.file = File(TEST_PATH)
        self.file2 = File(TEST_PATH2)

    def test_basedir(self):
        basedir = File.basedir(__file__)
        self.assertEqual(basedir, Path(__file__).parent)

    def test_repr(self):
        self.assertEqual(repr(self.file), f'File(path="{TEST_PATH}")')

    def test_str(self):
        self.assertEqual(str(self.file), TEST_PATH)

    def test_eq(self):
        file2 = File(TEST_PATH)
        self.assertTrue(self.file == file2)

    def test_no_eq(self):
        self.assertFalse(self.file == self.file2)

    def test_wrong_class_eq(self):
        self.assertFalse(self.file == 2)

    def test_str_eq(self):
        self.assertTrue(self.file == self.file.path)
        
    def test_name(self):
        self.assertEqual(self.file.name, 'test.csv')
