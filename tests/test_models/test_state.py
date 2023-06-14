"""testing module using unittest
This module exclusively tests the state module
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.state import State
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
        self.state = State()

    def tearDown(self):
        """operations that need to happen at the end of each test"""
        del self.state

    def test_name(self):
        """ test name attribute """
        self.assertEqual(self.state.name, "")
        self.state.name = "testname"
        self.assertEqual(self.state.name, "testname")


if __name__ == '__main__':
    unittest.main
