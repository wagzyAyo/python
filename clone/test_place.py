#!/usr/bin/python3
"""test file for Place Class"""
import unittest
from place import Place


class TestPlace(unittest.TestCase):
    """Test case for Place Class"""

    def test_default(self):
        """test for default value"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.a
