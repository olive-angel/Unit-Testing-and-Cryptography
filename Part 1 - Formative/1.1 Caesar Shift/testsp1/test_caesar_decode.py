from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode
class TestCaesarDecode(TestCase):
    def test_caesar_decode_two_parameters_with_uppercase(self):
        self.assertEqual(caesar_decode("MJQQTBTWQI", 5), "HELLOWORLD")
    def test_caesar_decode_two_parameters_with_lowercase(self):
        self.assertEqual(caesar_decode("mjqqtbtwqi", 5), "HELLOWORLD")

    def test_caesar_encode_with_

    def test_caesar_encode_with_