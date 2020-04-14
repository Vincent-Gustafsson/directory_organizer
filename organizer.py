from argparse import ArgumentParser
from pathlib import Path
from typing import List

# The subdirs you want to have.
# The keys are what you refer to in the code
# The Values are the actual names of the subdirs that get creatad.
subdirs = {
    "images": "images",
    "videos": "videos",
    "exe_zip": "exe_zip",
    "audio": "audio",
    "other": "other"
}

# These are the "actions".
# The keys are the file extensions you want to move into the specified dir.
# The values are the dir you want the files with the extension to go in to.
actions = {
    ".png": subdirs["images"],
    ".jpg": subdirs["images"],
    ".gif": subdirs["images"],

    ".mp4": subdirs["videos"],
    ".mov": subdirs["videos"],
    ".avi": subdirs["videos"],

    ".exe": subdirs["exe_zip"],
    ".rar": subdirs["exe_zip"],
    ".zip": subdirs["exe_zip"],

    ".wav": subdirs["audio"],
    ".mp3": subdirs["audio"],
    ".ogg": subdirs["audio"],
    ".flac": subdirs["audio"],
}


def create_subdirs(dir: Path, subdirs: List[Path]):
    for subdir in subdirs:
        (dir / subdir).mkdir(exist_ok=True)


def organize_dir(dir: Path):
    # dir.glob("*,*") is used to get all the files (and subdirs) in the directory.
    for file in dir.glob("*.*"):
        if file.is_file():
            # If the file has an extension that's in the actions and destination, move the file.
            try:
                dest_path = dir / actions[file.suffix] / file.name            
            # If the file doesn't have an extension, move it into the "other" dir. 
            except KeyError:
                dest_path = dir / subdirs["other"] / file.name
            
            file.rename(dest_path)


def main():
    parser = ArgumentParser()
    parser.add_argument('dir', type=str, metavar='PATH', help='Path to the directory to organize.')
    args = parser.parse_args()
    args.dir = Path(args.dir)

    # check if the directory exists
    if not args.dir.is_dir():
        raise ValueError(f'Directory {str(args.dir)} is not an actual directory.')

    # create the subdirectories (if they do not exist yet)
    create_subdirs(args.dir, list(subdirs.values()))
    
    organize_dir(args.dir)


if __name__ == "__main__":
    main()
