from pathlib import Path
from pprint import pprint

# === HOME DIRECTORIES LIST COMPREHENSION
home_directories = [
    x for x in Path.home().iterdir()
    if (x.is_dir() and not x.name.startswith("."))
        ]

# === HOME DIRECTORIES GENERATOR ===

home_directories_gen = (
    x for x in Path.home().iterdir()
    if (x.is_dir() and not x.name.startswith("."))
)

# === VERSION DICT COMPREHENSION === 
home_directories_dict = {
    number:directory for number, directory in enumerate(home_directories, 1)
}

# === VERSION FOR === 

home_directories_dict2 = {}
for number, directory in enumerate(home_directories, 1):
    home_directories_dict2[number] = directory
    
def display_files(n, format):
    directory = home_directories_dict2[n]
    files = directory.glob(f"*.{format}")
    return [file for file in files]

if __name__ == '__main__':
    #print("Choose the directory you want to work with:")
    #pprint(home_directories_dict2)
    #directory_n = int(input()) 
    #pprint(display_files(directory_n, "xlsx")) 

    print(next(home_directories_gen))
    print(next(home_directories_gen))
    print(next(home_directories_gen))
    print(type(home_directories_gen))
