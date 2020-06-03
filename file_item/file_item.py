from typing import Optional
from pathlib import Path
import os


class File:
    """
    File object
    """

    def __init__(self, path: str) -> None:
        """
        :param str path: file's absolute path
        """
        self.path = path if path is not None else os.path.join('.', self.name)

    @property
    def name(self) -> str:
        """File name"""
        return Path(self.path).name

    def __repr__(self):
        return f'File(path="{self.path}")'

    def __str__(self):
        return self.path

    def __eq__(self, other):
        if isinstance(other, self.__class__) or isinstance(other, str):
            return self.path == other
        return False

    @staticmethod
    def basedir(file_: str) -> str:
        """
        Return file's basedir

        :param str file_: path to a file
        :return: path to the file's folder

        Example:
            >>> from file_item import File
            >>> basedir = File.basedir(__file__)
        """
        return Path(file_).parent
