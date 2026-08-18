import logging
from pprint import pprint
from utilities import find_dir, temporary_test_copy, dict_testing

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


def main():
    test_dir = find_dir("Downloads")
    test_copy_dir = temporary_test_copy(test_dir)
    pprint(dict_testing(test_copy_dir))


main()
