from pathlib import Path
import os


class File:
    @staticmethod
    def basedir(file_: str) -> str:
        return Path(file_).parent
