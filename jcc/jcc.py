#!/usr/bin/env python3

"""
A simple python script to take all the java classes in a directory and output them in a single file
"""

from argparse import ArgumentParser
import os

def set_clipboard(text: str) -> str:
    """
    Set the clipboard to the given text using xclip
    Returns the text that was set to the clipboard for testing.
    """
    os.system("echo \"" + text + "\" | xclip -rmlastnl -selection clipboard")
    return text

def get_classes(folder: str, excl, main: bool = False) -> str:
    """
    Get all the classes in a folder
    """
    files = ""
    lines = ""
    for file in os.listdir(folder):
        if file.endswith(".java") and (file not in excl):
            f = open((folder + file), "r")
            for line in f.readlines():
                if not line.startswith("import "):
                    lines += line
            lines += "\n"
            f.close()
    return(lines)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('folder', help='The folder to parse')
    parser.add_argument(
        "-m", "--main", help="do not ignore the main class", action="store_true"
    )
    parser.add_argument(
        "-e", "--exclude", nargs='*', help="exclude specified class or classes by name (is case sensitive)"
    )
    args = parser.parse_args()

    if args.exclude == None:
        args.exclude = []
    classes = get_classes(args.folder, args.exclude, args.main)
    print(classes)