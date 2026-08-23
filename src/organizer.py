from pathlib import Path
from utilities import DirContext
from pprint import pprint
import logging, shutil

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
            if extension not in dir_dict["dirs"]:
                extension_path = self.context.full_path / Path(
                    extension.replace(".", "")
                )
                extension_path.mkdir()

            for file in dir_dict["files"][extension]:
                try:
                    shutil.move(self.context.full_path / file, extension_path)
                except Exception as e:
                    logger.warning("Couldn't move file:\n%s", e)


if __name__ == "__main__":
    context_test = DirContext("Downloads_copy")
    organizer_test = Organizer(context_test)
    organizer_test.organizer()
