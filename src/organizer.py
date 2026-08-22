from pathlib import Path
from utilities import DirContext
from pprint import pprint
import logging, shutil

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Organize:
    def __init__(self, directory) -> None:
        self.directory = directory

    def organizer(self, dict_dir):

        if not self.directory:
            return
        
    for file in self.directory.iterdir():
        

if __name__ == "__main__":
    path_test = DirContext("Downloads")
