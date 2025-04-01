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
    os.system(
        "echo \"" +
        text.replace('\"', '\\\"') +
        "\" |" + 
        "xclip -rmlastnl -selection clipboard"
    )
    return text

def get_classes(folder: str, excl, main: bool = False) -> str:
    """
    Get all the classes in a folder
    """
    files = ""
    lines = ""
    import_lines = [""]
    package_lines = [""] # samesies
    for file in os.listdir(folder):
        if file.endswith(".java") and (file not in excl):
            f = open((folder + file), "r", encoding="utf-8")
            for line in f.readlines():
                if line.startswith("import "):
                    import_lines.append(line)
                elif line.startswith("package "):
                    package_lines.append(line)
                else:
                #if not line.startswith("import ") and not line.startswith("package "):
                    lines += line
            lines += "\n"
            f.close()
    import_lines = list(set(import_lines))
    package_lines = list(set(package_lines))
    # TODO: implement import and package parser choice to be added to the parameters, for now it only adds import bc i dont need package rn 
    lines = "".join(import_lines) + lines
    return lines

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('folder', help='The folder to parse')
    parser.add_argument(
        "-m",
        "--main",
        help="do not ignore the main class",
        action="store_true"
    )
    parser.add_argument(
        "-e",
        "--exclude",
        nargs='*',
        help="exclude specified class or classes by name (is case sensitive)"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output file",
        action="store_true"
    )
    parser.add_argument(
        "-i",
        "--import",
        help="include import statements",
        action="store_true"
    )
    parser.add_argument(
        "-p",
        "--package",
        help="include package statement",
        action="store_true"
    )
    args = parser.parse_args()

    if args.exclude is None:
        args.exclude = []
    classes = get_classes(args.folder, args.exclude, args.main) #TODO: import and package parser arg to be added to the parameters maybe
    set_clipboard(classes)

    if args.output:
        print(classes)
