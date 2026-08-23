from utilities import DirContext


context = DirContext("Downloads_copy")
directory_dict = context.dict_dir()

print(type(directory_dict["files"]))

print(directory_dict.values())
