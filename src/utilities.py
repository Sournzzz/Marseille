import shutil, logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class DirContext:
    def __init__(self, dir_path):
        self.dir_path = Path(dir_path)
        self.home_path = Path.home()
        self.full_path = self.home_path / self.dir_path

    def find_dir(self):
        logger.info("Looking for: %s", self.full_path)

        if self.full_path.exists():
            logger.info("Directory found: %s", self.full_path)
            return True

        logger.warning("Directory not found %s", self.full_path)

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

            return True

        except FileExistsError:
            logger.error(
                "The %s directory already exists. Couldn't make a copy.",
                self.full_path.name,
            )

            return False

    def dict_dir(self):
        pass


def temporary_test_copy(directory):
    if not directory:
        logger.error("Directory doesn't exist, couln't make a copy")
        return
    directory_name = directory.name + "_test"
    destination_directory = directory.parent / directory_name

    try:
        logger.info("Starting copy of the [%s] directory", directory.name)
        shutil.copytree(directory, destination_directory)

    except FileExistsError:
        logger.error(
            "The [%s] directory already exists. Couldn't make copy.", directory_name
        )

    return destination_directory


def find_dir(dir_name: str) -> Path | None:

    path = Path.home() / dir_name

    logger.info("Looking for: %s", dir_name)

    for directory in Path.home().iterdir():
        if directory == path:
            logger.info("Path found: %s", path)
            return path

    logger.error("%s: Directory not found", dir_name)
    return None


def dict_testing(directory: Path):
    if not directory:
        return
    result = {}
    result["files"] = [
        Path(file.name) for file in directory.iterdir() if file.is_file()
    ]
    result["dirs"] = [
        Path(folder.name) for folder in directory.iterdir() if folder.is_dir()
    ]

    return result


if __name__ == "__main__":
    directory = DirContext("Downloads")
    directory.find_dir()
    directory.copy_dir()
