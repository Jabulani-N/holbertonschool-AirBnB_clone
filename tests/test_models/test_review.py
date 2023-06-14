"""testing module using unittest
This module exclusively tests the review module
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.review import Review
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
        self.review = Review()

    def tearDown(self):
        """operations that need to happen at the end of each test"""
        del self.review

    def test_place_id(self):
        """ test place_id attribute """
        self.assertEqual(self.review.place_id, "")
        self.review.place_id = "testplace_id"
        self.assertEqual(self.review.place_id, "testplace_id")

def test_user_id(self):
        """ test user_id attribute """
        self.assertEqual(self.review.user_id, "")
        self.review.user_id = "testuser_id"
        self.assertEqual(self.review.user_id, "testuser_id")

if __name__ == '__main__':
    unittest.main
