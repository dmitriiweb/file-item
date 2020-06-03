from pathlib import Path
import os


class File:
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
