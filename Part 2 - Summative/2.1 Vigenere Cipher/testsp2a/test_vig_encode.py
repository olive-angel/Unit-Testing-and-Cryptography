from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class TestVigEncode(TestCase):

    def test_vig_encode_with_text_and_keyword_uppercase(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", "TEST"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")

    def test_vig_encode_with_text_and_keyword_lowercase(self):
        self.assertEqual(vig_encode("thequickbrownfoxjumpedoverthelazydog", "test"), "MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ")
