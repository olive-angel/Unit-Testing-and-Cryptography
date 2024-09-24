from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode


class TestAffineDecode(TestCase):

    def test_affine_decode_with_uppercase_text(self):
        self.assertEqual(affine_decode("EVQQZXZIQS", 3, 9), "HELLOWORLD")

    def test_affine_decode_with_uppercase_text(self):
        self.assertEqual(affine_decode("evqqzxziqs", 3, 9),"HELLOWORLD")
