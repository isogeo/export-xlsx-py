# -*- coding: UTF-8 -*-
#! python3

"""
    Usage from the repo root folder:

    ```python
    # for whole test
    python -m unittest tests.test_i18n
    # for specific
    python -m unittest tests.test_i18n.Testi18n.test_translations_length
    ```
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import unittest

# target
from isogeotoxlsx.i18n import I18N_EN, I18N_FR


# #############################################################################
# ########## Classes ###############
# ##################################


class Testi18n(unittest.TestCase):
    """Test minimalist translation module."""

    def setUp(self):
        """Executed before each test."""
        pass

    def tearDown(self):
        """Executed after each test."""
        pass

    # -- TESTS ---------------------------------------------------
    def test_translations_length(self):
        """Ensure that different translations have the same length"""
        self.assertEqual(len(I18N_EN), len(I18N_FR))

    def test_translations_values(self):
        """Ensure that different translations have the same length"""
        # check basic values
        self.assertTrue(I18N_EN.get("title") == "Title")
        self.assertTrue(I18N_FR.get("title") == "Titre")
        # check if every key has a value
        for k in I18N_EN:
            self.assertIsNotNone(I18N_EN.get(k))
            self.assertNotEqual(I18N_EN.get(k), "")
        for k in I18N_FR:
            self.assertIsNotNone(I18N_FR.get(k))
            self.assertNotEqual(I18N_FR.get(k), "")


# #############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    unittest.main()
