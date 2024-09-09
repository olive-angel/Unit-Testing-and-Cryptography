from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode
class TestCaesarEncode(TestCase):

    def test_caesar_encode_with_two_parameters_with_uppercase(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 5), "MJQQTBTWQI")

    def test_caesar_encode_with_two_parameters_with_lowercase(self):
        self.assertEqual(caesar_encode("helloworld", 5), "MJQQTBTWQI")

    def test_caesar_encode_with_empty_second_parameter(self):
        self.assertEqual(caesar_encode("helloworld", None), "helloworld")

    def test_caesar_encode_with_empty_first_parameter(self):
        self.assertEqual(caesar_encode("", 5), "")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(caesar_encode("   ", 5), "   ")