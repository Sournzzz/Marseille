from pathlib import Path
from utilities import DirContext
from pprint import pprint
import logging, shutil, regex as re

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Organizer:
    def __init__(self, context: DirContext) -> None:
        self.context = context

    def organizer(self):
        logger.info("Ensuring the directory")

        if not self.context:
            logger.warning("Couldn't find %s", self.context)
            return

        dir_dict = self.context.dict_dir()

        for extension in dir_dict["files"]:
            if extension not in dir_dict["dirs"].lower():
                extension_path = self.context.full_path / extension.replace(".", "")
            else:
                dir_index = dir_dict["dirs"].index(extension)
                extension_path = self.context.full_path / dir_dict["dirs"][dir_index]

            extension_path.mkdir()

            for file in dir_dict["files"][extension]:
                if (self.context.full_path / extension_path / file).exists():
                    pass

                shutil.move(self.context.full_path / file, extension_path)

    def file_dname_formatter(self, file):
        # I NEED TO SEPARATE THE  NUMBER OF (n) from the file name and verify it first
        compound_suffixes = self.context.common_compound_suffixes

        fsuffixes = file.suffixes
        fname = file.name.split(".")[0]
        fpattern = re.search(r"\(\d+\)", file.name)

        if fpattern:
            index1, index2 = fpattern.span()
            file_number = re.search(r"\d+", file.name[index1:index2])
            new_file_number = str(int(file_number.group()) + 1)
            file = file.parent / file.name.replace(file_number.group(), new_file_number)

        if len(fsuffixes) > 2 and "".join(fsuffixes) in compound_suffixes:
            filename = file.name


if __name__ == "__main__":
    context_test = DirContext("Downloads_copy")
    organizer_test = Organizer(context_test)

    organizer_test.organizer()
