import os
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        return self.file

    def __exit__(self, exc_type: None, exc_val: None,
                 exc_tb: None) -> Optional[type[BaseException]]:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.file.close()


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
