"""from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_encode


class TestAffineNEncode(TestCase):

    def test_affine_n_encode_with_uppercase_text(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", ))

    def test_affine_n_encode_with_lowercase_text(self):
        self.assertEqual(affine_n_encode("thequickbrownfoxjumpedoverthelazydog"), )
"""