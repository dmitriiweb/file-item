from typing import Optional
from pathlib import Path
import os


class File:
    """
    File object
    """
    def __init__(self, name: str, path: Optional[str] = None) -> None:
        """
        :param str name: file's name
        :param str path: file's absolute path
        """
        self.name = name
        self.path = path if path is not None else os.path.join('.', self.name)

    def __repr__(self):
        return f'File(name="{self.name}", path="{self.path}")'

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
