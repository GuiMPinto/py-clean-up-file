import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        return

    def __exit__(self, exc_type: type[BaseException] | None,
                 exc_val: type[BaseException] | None,
                 exc_tb: type[BaseException] | None) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
