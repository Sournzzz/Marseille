from pathlib import Path
from utilities import DirContext
from pprint import pprint
import logging, shutil, re

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Organizer:
    def __init__(self, context: DirContext) -> None:
        self.context = context

    def organizer(self) -> None:
        logger.info("Ensuring the directory")

        dir_dict = self.context.dict_dir()

        if not dir_dict:
            logger.warning("Couldn't create dir for: %s", self.context.full_path)
            return

        existing_dirs = {d.name.lower(): d for d in dir_dict["dirs"]}

        for extension in dir_dict["files"]:
            if extension in existing_dirs:
                extension_path = self.context.full_path / existing_dirs[extension]
            else:
                extension_path = self.context.full_path / extension

            extension_path.mkdir(exist_ok=True)

            for file in dir_dict["files"][extension]:
                if (extension_path / file).exists():
                    new_name = self.file_dname_formatter(file)
                    file.rename(new_name)

                shutil.move(self.context.full_path / file, extension_path)

    def file_dname_formatter(self, converted_file: Path) -> Path:
        # I NEED TO SEPARATE THE  NUMBER OF (n) from the file name and verify it first

        compound_suffixes = self.context.common_compound_suffixes

        fpattern = re.search(r".*\(\d+\)", converted_file.name)

        if fpattern:
            index1, index2 = fpattern.span()
            converted_file_number = re.search(
                r"\d+", converted_file.name[index1:index2]
            )
            new_file_number = str(int(converted_file_number.group()) + 1)
            converted_file = converted_file.parent / converted_file.name.replace(
                converted_file_number.group(), new_file_number
            )
        else:
            if (
                len(converted_file.suffixes) > 2
                and "".join(converted_file.suffixes) in compound_suffixes
            ):
                fname = (
                    converted_file.name.split(".")[0]
                    + "(1)"
                    + "".join(converted_file.suffixes)
                )
                converted_file = converted_file.parent / fname

            fname = converted_file.stem + "(1)" + converted_file.suffix
            converted_file = converted_file.parent / fname

        # HERE GOES IN CASE THE FILE EXISTS BUT DOESN'T HAVE ALREADY A "(n)" INSIDE THE FOLDER

        return converted_file


if __name__ == "__main__":
    context_test = DirContext("Downloads_copy")
    organizer_test = Organizer(context_test)

    organizer_test.organizer()
