from typing import Optional, Union
from pathlib import Path, PosixPath
import os


class File:
    """
    File object
    """

    def __init__(self, path: Union[str, PosixPath]) -> None:
        """
        :param str path: file's absolute path
        """
        if isinstance(path, str):
            self.path = Path(path)
        elif isinstance(path, PosixPath):
            self.path = path
        else:
            raise ValueError(f'The path variable should be str or PosixPath, not {type(path)}')

    @property
    def name(self) -> str:
        """File name"""
        return Path(self.path).name

    def __repr__(self):
        return f'File(path="{self.path}")'

    def __str__(self):
        return str(self.path)

    def __eq__(self, other: Union['File', PosixPath, str]):
        if isinstance(other, self.__class__):
            return self.path == other.path
        elif isinstance(other, PosixPath):
            return self.path == other
        elif isinstance(other, str):
            return str(self.path) == other
        return False

    def create_folder(self):
        pass

    @staticmethod
    def basedir(file_: str) -> PosixPath:
        """
        Return file's basedir

        :param str file_: path to a file
        :return: path to the file's folder

        Example:
            >>> from file_item import File
            >>> basedir = File.basedir(__file__)
        """
        return Path(file_).parent
