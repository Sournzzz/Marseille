import logging, argparse
from organizer import Organizer
from utilities import DirContext


logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


def parse_args() -> argparse.Namespace:
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


def main(args: argparse.Namespace) -> int | None:
    match args.command:
        case "organizer":
            path_context = DirContext(args.path)

            if not path_context.find_dir():
                return 1

            if args.no_copy:
                organize = Organizer(path_context)
                organize.organizer()
                return 0

            path_context.copy_dir()
            organize = Organizer(path_context)
            organize.organizer()
            return 0


if __name__ == "__main__":
    args = parse_args()
    main(args)
