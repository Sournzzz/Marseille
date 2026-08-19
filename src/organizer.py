from pathlib import Path
from utilities import dict_testing, find_dir
from pprint import pprint


class Organize:
    def __init__(self, directory: Path | None) -> None:
        self.directory = directory

    def organizer(self):
        if not self.directory:
            return

    def get_extensions(self):
        test_dict = dict_testing(self.directory)

        # I'M GOING TO MANAGE SOME EDGE CASES AT THE MOMENT
        test_dict["file_extensions"] = [
            "".join(ext.suffixes) for ext in test_dict["files"]
        ]

        return test_dict


if __name__ == "__main__":
    organizer_test = Organize(find_dir("Downloads_test"))
    pprint(organizer_test.get_extensions())
