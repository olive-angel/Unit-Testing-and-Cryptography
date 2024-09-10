from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode

class TestSubDecode(TestCase):
    def test_sub_decode_two_strings_with_uppercase(self):
        self.assertEqual(sub_decode(
    def test_sub_decode_two_strings_with_lowercase(self):
        self.assertEqual(sub_decode(

    def test_sub_decode_with_empty_second_parameter(self):
        self.assertEqual(sub_decode(

    def test_sub_decode_with_empty_first_parameter(self):
        self.assertEqual(sub_decode(

    def test_sub_decode_with_whitespace(self):
        self.assertEqual(sub_decode(