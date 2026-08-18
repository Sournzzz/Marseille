import shutil, logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def temporary_test_copy(directory):
    if not directory:
        logger.error("Directory doesn't exist, couln't make a copy")

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

    result = {}
    result["files"] = [file.name for file in directory.iterdir() if file.is_file()]
    result["dirs"] = [folder.name for folder in directory.iterdir() if folder.is_dir()]

    return result


if __name__ == "__main__":
    directory = find_dir("Downloads")
    print(directory)
    temporary_test_copy(directory)
