#!/usr/bin/python3
"""test file for City Class"""
import unittest
from city import City


class TestCity(unittest.TestCase):
    """Tests Cases for city class"""

    def test_default(self):
        """Check for default attr"""
        city = City
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_type(self):
        """Test City attributes type"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_attribute(self):
        """check the city class Atrributes"""
        city = City
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))


if __name__ == "__main__":
    unittest.main()
