from pathlib import Path
from utilities import DirContext
import logging, shutil, re

"""
THIS IS THE ORGANIZER TOOL
MAKES A COPY AND OPERATES ON IT IF NOT INDICATED 
"""


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Organizer:
    def __init__(self, context: DirContext) -> None:
        self.context = context

    """
    THIS IS THE MAIN TOOL, NEED SOME REFACTORING
    IT IS SLOW TO DETECT MULTIPLE DUPLICATED FILES 
    """

    def organizer(self) -> None:
        logger.info("Ensuring the directory...")

        dir_dict = self.context.dict_dir()

        if not dir_dict:
            logger.warning("Couldn't create dir for: %s", self.context.full_path)
            return

        logger.info("Starting the organization...")
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

                    while (extension_path / new_name).exists():
                        new_name = self.file_dname_formatter(new_name)

                    source_name = self.context.full_path / file
                    new_path = self.context.full_path / new_name

                    source_name.rename(new_path)
                    shutil.move(new_path, extension_path)

                    logger.warning(
                        "File already existed in the destiny dir, made a copy: %s to %s",
                        file.name,
                        new_path.name,
                    )

                else:
                    shutil.move(self.context.full_path / file, extension_path)

        logger.info("DONE!")

    def file_dname_formatter(self, converted_file: Path) -> Path:
        """
        THIS FORMATTER USES REGEX
        COVERS THE EDGE CASE OF file(1) EXISTS SO file(1) -> file(2)
        OR file EXISTS SO file -> file(1)
        """

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

        return converted_file
