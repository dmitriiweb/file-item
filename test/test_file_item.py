from pathlib import Path
import unittest

from file_item import File


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_basedir(self):
        basedir = File.basedir(__file__)
        self.assertEqual(basedir, Path(__file__).parent)

