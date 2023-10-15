#!/usr/bin/python3
"""This module contains Test cases for user class"""
import unittest
from base import BaseModel
from user import User


class TestUser(unittest.TestCase):
    """test cases for user class"""

    def test_inherit(self):
        """Test the user class inherits from base model"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_check(self):
        """Check if user has attribute"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_default(self):
        """Check default attribute for user class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.last_name, "")

    def test_type(self):
        """Check the type of each user attribute"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.password, str)


if __name__ == "__main__":
    unittest.main()
