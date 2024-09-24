from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode


class TestAffineEncode(TestCase):
    def test_affine_encode_with_uppercase_text(self):
        self.assertEqual(affine_encode("HELLOWORLD", 3, 9),"EVQQZXZIQS")

    def test_affine_encode_with_lowercase_text(self):
        self.assertEqual(affine_encode("helloworld", 3, 9), "EVQQZXZIQS")
