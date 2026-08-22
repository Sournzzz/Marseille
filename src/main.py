import logging
from pprint import pprint
from utilities import DirContext


logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


def main():
    test_dir = DirContext("Downloads")
    test_dir.find_dir()
    test_dir.copy_dir()
    pprint(test_dir.dict_dir2())


main()
