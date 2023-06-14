"""testing module using unittest
This module exclusively tests the file_storage module
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.user import User
import os
import json
import io
import sys

# items below are imported for unittest.mock
import uuid
import datetime


class TestFileStorage(unittest.TestCase):
    """test class for file_storage.py"""

    def setUp(self):
        """operations that need to happen each test will happen here"""
        self.user = User()

    def tearDown(self):
        """operations that need to happen at the end of each test"""
        del self.user

    def test_email(self):
        """ test email attribute """
        self.user.email = "testmail"
        self.assertEqual(self.user.email, "testmail")

    def test_password(self):
        """ test password attribute """
        self.user.password = "testword"
        self.assertEqual(self.user.password, "testword")

    def test_first(self):
        """ test first_name attribute """
        self.user.first_name = "testfirst"
        self.assertEqual(self.user.first_name, "testfirst")

    def test_last(self):
        """ test last_name attribute """
        self.user.last_name = "testlast"
        self.assertEqual(self.user.last_name, "testlast")


if __name__ == '__main__':
    unittest.main
