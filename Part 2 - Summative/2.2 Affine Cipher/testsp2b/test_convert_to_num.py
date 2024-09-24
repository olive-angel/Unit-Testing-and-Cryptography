from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num


class TestConvertToNum(TestCase):
    def test_convert_to_num_with_uppercase_text(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", len("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")), 218741750267309021256255930435388550208768849997977)

    def test_convert_to_num_with_lowercase_text(self):
        self.assertEqual(convert_to_num("thequickbrownfoxjumpedoverthelazydog", len("thequickbrownfoxjumpedoverthelazydog")), 218741750267309021256255930435388550208768849997977)

