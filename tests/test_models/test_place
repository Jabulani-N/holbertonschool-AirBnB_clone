"""testing module using unittest
This module exclusively tests the city module
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.city import City
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
        self.city = City()

    def tearDown(self):
        """operations that need to happen at the end of each test"""
        del self.city

    def test_name(self):
        """ test name attribute """
        self.assertEqual(self.city.name, "")
        self.city.name = "testname"
        self.assertEqual(self.city.name, "testname")

def test_state_id(self):
        """ test state_id attribute """
        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "teststate_id"
        self.assertEqual(self.city.state_id, "teststate_id")

if __name__ == '__main__':
    unittest.main
