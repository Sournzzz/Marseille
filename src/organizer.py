from pathlib import Path


class Organize:
    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def organizer(self):
        dir_tracker = []

        for file in self.directory.iterdir():
            pass
