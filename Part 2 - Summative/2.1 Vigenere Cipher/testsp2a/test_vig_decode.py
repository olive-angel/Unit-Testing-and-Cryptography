from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode


class TestVigDecode(TestCase):

    def test_vig_decode_with_text_and_keyword_lowercase(self):
        self.assertEqual(

    def test_vig_decode_with_text_and_keyword_uppercase(self):
        self.assertEqual(
