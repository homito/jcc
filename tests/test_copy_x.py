import unittest
import subprocess

import sys
import os

# Add the path to jcc.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../jcc')))
from jcc import set_clipboard


class TestCopyX(unittest.TestCase):
    def test_unittest(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 0)

    def test_set_clipboard(self):
        arg = "xclip -o -selection clipboard"

        self.assertEqual(
            set_clipboard("copied text"),
            subprocess.run(arg, shell=True, capture_output=True, text=True, check=True).stdout
        )

        self.assertEqual(
            set_clipboard("copied\n text\n"),
            subprocess.run(arg, shell=True, capture_output=True, text=True, check=True).stdout
        )

if __name__ == "__main__":
    unittest.main()
