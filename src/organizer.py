from pathlib import Path
from utilities import dict_testing, find_dir
from pprint import pprint


class Organize:
    common_compound_suffixes = [
        ".tar.gz",
        ".tar.bz2",
        ".tar.txz",
        ".tar.zst",
        ".tar.lz",
        ".tar.Z",
        ".mesh.xml",
        ".skeleton.xml",
    ]

    def __init__(self, directory) -> None:
        self.directory = directory

    def organizer(self):
        if not self.directory:
            return

    def get_extensions(self):

        test_dict = dict_testing(self.directory)

        # I'M GOING TO MANAGE SOME EDGE CASES AT THE MOMENT

        test_dict["extensions"] = set()
        for file in test_dict["files"]:
            suffix_tracker = file.suffixes

            if (
                len(suffix_tracker) > 2
                and "".join(suffix_tracker) in self.common_compound_suffixes
            ):
                test_dict["extensions"].add("".join(suffix_tracker).lower())

            elif file.suffix:
                test_dict["extensions"].add(file.suffix.lower())

            else:
                continue  # Here goes a logging

        return test_dict


if __name__ == "__main__":
    dir_path_test = find_dir("Downloads_test")
    organizer_test = Organize(dir_path_test)
    pprint(organizer_test.get_extensions())
