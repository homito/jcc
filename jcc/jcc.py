#!/usr/bin/env python3

"""
A simple python script to take all the java classes in a directory and output them in a single file
"""

from argparse import ArgumentParser
import os
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk


def copy_text(text: str):
    #self.clipboard.set_text(self.entry.get_text(), -1)
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    #clipboard.set_text(text, -1)
    print(clipboard)


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
    return lines

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
    copy_text(classes)
    print(classes)