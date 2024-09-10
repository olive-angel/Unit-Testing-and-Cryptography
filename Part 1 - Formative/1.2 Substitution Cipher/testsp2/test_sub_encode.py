from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestSubEncode(TestCase):
    def test_sub_encode_two_strings_with_uppercase(self):
        self.assertEqual(sub_encode("HELLOWORLD","WJKUXVBMIYDTPLHZGONCRSAEFQ"),  "MXTTHAHOTU")

    def test_sub_encode_two_strings_with_lowercase(self):
        self.assertEqual(sub_encode("helloworld", "wjkuxvbmiydtplhzgoncrsaefq"), "MXTTHAHOTU")

    def test_sub_encode_with_empty_second_parameter(self):
        self.assertEqual(sub_encode

    def test_sub_encode_with_empty_first_parameter(self):
        self.assertEqual(sub_encode

    def test_sub_encode_with_whitespace(self):
        self.assertEqual(sub_encode