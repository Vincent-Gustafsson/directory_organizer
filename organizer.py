from pathlib import Path

# The folder you want to organize
directory = Path("C:/Users/Vincent/Downloads")

# The folders you want to have.
# The keys are what you refer to in the code
# The Values are the actual names of the folders that get creatad.
folders = {
    "images": "images",
    "videos": "videos",
    "exe_zip": "exe_zip",
    "audio": "audio",
    "other": "other"
}

# These are the "actions".
# The keys are the file extensions you want to move into the specified folder.
# The values are the folder you want the files with the extension to go in to.
actions = {
    ".png": folders["images"],
    ".jpg": folders["images"],
    ".gif": folders["images"],

    ".mp4": folders["videos"],
    ".mov": folders["videos"],
    ".avi": folders["videos"],

    ".exe": folders["exe_zip"],
    ".rar": folders["exe_zip"],
    ".zip": folders["exe_zip"],

    ".wav": folders["audio"],
    ".mp3": folders["audio"],
    ".ogg": folders["audio"],
    ".flac": folders["audio"],
}


def create_directories(dir):
    for dir_name in folders.values():
        if dir.joinpath(dir_name) not in dir.iterdir():
            dir.joinpath(dir_name).mkdir()


def organize_folder(dir):
    dir = Path(dir)

    # dir.glob("*,*") is used to get all the files (and folders) in the directory.
    for file in dir.glob("*.*"):
        if file.is_file():
            # If the file has an extension that's in the actions and destination, move the file.
            try:
                dest_path = dir.joinpath(actions[file.suffix], file.name)
                file.rename(dest_path)
            
            # If the file doesn't have an extension, move it into the "other" folder. 
            except KeyError:
                dest_path = dir.joinpath(folders["other"], file.name)
                file.rename(dest_path)


if __name__ == "__main__":
    # This function checks if the sub-folders exists. If they don't, create them.
    create_directories(directory)
    
    organize_folder(directory)

