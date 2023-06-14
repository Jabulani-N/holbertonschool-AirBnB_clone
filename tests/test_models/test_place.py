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

    def test_description(self):
        """ test description attribute """
        self.assertEqual(self.place.description, "")
        self.place.description = "testdescription"
        self.assertEqual(self.place.description, "testdescription")

    def test_number_rooms(self):
        """ test number_rooms attribute """
        self.assertEqual(self.place.number_rooms, 0)
        self.place.number_rooms = 4
        self.assertEqual(self.place.number_rooms, 4)

    def test_number_bathrooms(self):
        """ test number_bathrooms attribute """
        self.assertEqual(self.place.number_bathrooms, 0)
        self.place.number_bathrooms = 2
        self.assertEqual(self.place.number_bathrooms, 2)

    def test_max_guest(self):
        """ test max_guest attribute """
        self.assertEqual(self.place.max_guest, 0)
        self.place.max_guest = 6
        self.assertEqual(self.place.max_guest, 6)

    def test_price_by_night(self):
        """ test price_by_night attribute """
        self.assertEqual(self.place.max_guest, 0)
        self.place.price_by_night = 600
        self.assertEqual(self.place.price_by_night, 600)


if __name__ == '__main__':
    unittest.main
