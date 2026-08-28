import shutil
from pathlib import Path

# THIS GENERATOR WORKS SO IT FILTERS WHAT THE iterdir() GENERATOR INITIALLY RETURNS


# FIND THE FOLDER BY ITERATING OVER THE GENERATOR
def find_directory(directory):

    home_directories_gen = (
        x for x in Path.home().iterdir() if (x.is_dir() and not x.name.startswith("."))
    )

    while True:
        current_directory = next(home_directories_gen)
        if current_directory.name == directory:
            return current_directory


# MAKING A COPY OF THE FOLDER DEFINED SO I CAN WORK ON IT WITHOUT BREAKING MY PC
def temporary_copy(directory):
    directory_name = directory.name + "_test"
    destination_directory = directory.parent / directory_name
    shutil.copytree(directory, destination_directory)
    return destination_directory


# START ORDERING THE FOLDER
def move_files(directory):
    directory_tracker = []

    for file in directory.iterdir():
        current_directory_suffix = file.suffix.lower().lstrip(".")
        current_dir = directory / current_directory_suffix

        print(directory_tracker)

        if file.is_file() and current_directory_suffix not in directory_tracker:
            directory_tracker.append(current_directory_suffix)
            current_dir.mkdir()
            shutil.move(file, current_dir)

        elif file.is_file():
            shutil.move(file, current_dir)


if __name__ == "__main__":
    downloads_folder = find_directory("Downloads")
    temporary_copy_downloads = temporary_copy(downloads_folder)
    move_files(temporary_copy_downloads)

    # PARA MAÑANA AGREGAR EL SHUTIL.MOVE Y REFACTORIZAR LEVE
    # shutil.rmtree(temporary_downloads) # DELETING THE FOLDER, TEMPORARY, MADE FOR TESTS
