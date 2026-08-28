import logging, argparse
from os import path
from typing import Required
from organizer import Organizer
from utilities import DirContext


logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Marseille",
        description="A filesystem toolkit",
        epilog="GOODBYE",
    )

    subparser = parser.add_subparsers(dest="command", required=True)

    organizer_parser = subparser.add_parser(
        "organizer", help="Organize by file extensions by giving a directory path"
    )

    organizer_parser.add_argument("path")
    organizer_parser.add_argument("-n", "--no-copy", action="store_true")

    args = parser.parse_args()

    return args


def main(args):
    match args.command:
        case "organizer":
            if args.no_copy:
                pass
            path_context = DirContext(args.path)
            path_context.copy_dir()
            organize = Organizer(path_context)
            organize.organizer()


if __name__ == "__main__":
    args = parse_args()
    main(args)
