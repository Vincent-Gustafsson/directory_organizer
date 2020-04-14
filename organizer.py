import json
from argparse import ArgumentParser
from pathlib import Path
from typing import Dict, List


def load_subdirs(subdirs_file: Path) -> Dict[str, str]:
    return json.load(open(subdirs_file, 'r', encoding='utf-8'))


def create_subdirs(dir: Path, subdirs: List[Path]) -> None:
    for subdir in subdirs:
        (dir / subdir).mkdir(exist_ok=True)


def organize_dir(dir: Path, actions: Dict[str, str], other: str) -> None:
    # iterate over all files (and not subdirectories) in the directory
    for file in dir.glob("*.*"):
        if file.is_file():
            try:  # if the file has a "known" extension, move it to its proper destination
                file_dest = dir / actions[file.suffix.lower()] / file.name            
            except KeyError:  # if the file has an "unkown" extension, move it into the "other" subdirectory
                file_dest = dir / other / file.name
            
            # move the file
            file.rename(file_dest)


def main():
    parser = ArgumentParser()
    parser.add_argument('dir', type=str, metavar='PATH', help='Path to the directory to organize.')
    parser.add_argument('subdirs_file', type=str, metavar='PATH', help='Path to the JSON-file containing the subdirectories.')
    args = parser.parse_args()
    args.dir = Path(args.dir)
    args.subdirs_file = Path(args.subdirs_file)

    # check if the directory exists
    if not args.dir.is_dir():
        raise ValueError(f'Directory {str(args.dir)} is not an actual directory.')

    # check if the subdirs file is a JSON-file
    if not args.subdirs_file.suffix.lower() == '.json':
        raise ValueError(f'Subdirectories file {args.subdirs_file} is not an actual JSON-file.')
    
    # load the dictionary of subdirectories
    subdirs = load_subdirs(args.subdirs_file)

    # create a dictionary mapping file extensions to subdirectories
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

    # create the subdirectories (if they do not exist yet)
    create_subdirs(args.dir, list(subdirs.values()))
    
    # organize the directory
    organize_dir(args.dir, actions, subdirs["other"])


if __name__ == "__main__":
    main()
