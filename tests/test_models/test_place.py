"""testing module using unittest
This module exclusively tests the place module
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.place import Place
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
        self.place = Place()

    def tearDown(self):
        """operations that need to happen at the end of each test"""
        del self.place

    def test_name(self):
        """ test name attribute """
        self.assertEqual(self.place.name, "")
        self.place.name = "testname"
        self.assertEqual(self.place.name, "testname")

def test_city_id(self):
        """ test city_id attribute """
        self.assertEqual(self.place.city_id, "")
        self.place.city_id = "testcity_id"
        self.assertEqual(self.place.city_id, "testcity_id")

def test_user_id(self):
        """ test user_id attribute """
        self.assertEqual(self.place.user_id, "")
        self.place.user_id = "testuser_id"
        self.assertEqual(self.place.user_id, "testuser_id")

if __name__ == '__main__':
    unittest.main