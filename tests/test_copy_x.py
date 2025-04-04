import unittest
import subprocess

import sys
import os

# Add the path to jcc.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../jcc')))
from jcc import set_clipboard
from jcc import get_classes


class TestCopyX(unittest.TestCase):
    def test_set_clipboard(self):
        arg = "xclip -o -selection clipboard"

        self.assertEqual(
            set_clipboard("copied text"),
            subprocess.run(arg, shell=True, capture_output=True, text=True, check=True).stdout
        )

        self.assertEqual(
            set_clipboard("\'copied\'\n text\n"),
            subprocess.run(arg, shell=True, capture_output=True, text=True, check=True).stdout
        )

        self.assertEqual(
            set_clipboard("\"copied\"\n text\n"),
            subprocess.run(arg, shell=True, capture_output=True, text=True, check=True).stdout
        )

    def test_get_classes(self):
        folder = "data/jexample_proj/"
        java_folder = folder + "java/"
        reference_folder = folder + "ref/"

        excl = []
        main = False

        res_classes = get_classes(java_folder, excl, main)
        ref_classes = ""

        with open(reference_folder + "reference", "r", encoding="utf-8") as f:
            for line in f.readlines():
                ref_classes += line
        f.close()

        self.assertEqual(res_classes, ref_classes)

if __name__ == "__main__":
    unittest.main()
