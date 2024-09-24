from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text


class TestConvertToText(TestCase):
    def test_convert_to_text(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977, len("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

