import shutil, logging
from pathlib import Path
from constants import COMMON_COMPOUND_SUFFIXES
from pprint import pprint


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class DirContext:
    def __init__(self, dir_path):
        self.dir_path = Path(dir_path)
        self.home_path = Path.home()
        self.full_path = self.home_path / self.dir_path
        self.common_compound_suffixes = COMMON_COMPOUND_SUFFIXES

    def find_dir(self):
        logger.info("Looking for: %s", self.full_path)

        if self.full_path.exists():
            logger.info("Directory found: %s", self.full_path)
            return True

        logger.warning("Directory not found %s", self.full_path)
        return False

    def copy_dir(self):
        copy_dir_path = self.full_path.parent / (self.full_path.name + "_copy")

        try:
            logger.info(
                "Trying a copy of '%s' directory in '%s'",
                self.full_path.name,
                self.full_path.parent,
            )

            shutil.copytree(self.full_path, copy_dir_path)
            logger.info("Success! Created: %s", copy_dir_path)
            self.full_path = copy_dir_path

            return True

        except FileExistsError:
            logger.error(
                "The %s directory already exists. Couldn't make a copy.",
                self.full_path.name,
            )

            return False

    def dict_dir(self):
        dict_structure = {}

        dict_structure["dirs"] = [
            Path(folder.name) for folder in self.full_path.iterdir() if folder.is_dir()
        ]

        dict_structure["files"] = {}

        for file in self.full_path.iterdir():
            if file.is_file():
                suffix_tracker = file.suffixes

                if (
                    len(suffix_tracker) >= 2
                    and "".join(suffix_tracker).lower() in self.common_compound_suffixes
                ):
                    dict_structure["files"].setdefault(
                        "".join(suffix_tracker).lower().replace(".", ""), []
                    ).append(Path(file.name))

                elif file.suffix:
                    dict_structure["files"].setdefault(
                        file.suffix.lower().replace(".", ""), []
                    ).append(Path(file.name))

                else:
                    # NEED TO ADD A LOG HERE
                    continue

        return dict_structure


if __name__ == "__main__":
    directory = DirContext("Downloads")
    directory.find_dir()
    directory.copy_dir()
    pprint(directory.dict_dir())
