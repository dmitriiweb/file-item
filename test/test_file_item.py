from pathlib import Path
import unittest

from file_item import File


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self.file_ = File

    def test_basedir(self):
        basedir = self.file_.basedir(__file__)
        self.assertEqual(basedir, Path(__file__).parent)
