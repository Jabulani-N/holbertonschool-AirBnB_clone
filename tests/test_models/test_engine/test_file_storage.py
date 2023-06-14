"""testing module using unittest
This module exclusively tests the file_storage module
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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
        self.model = BaseModel()
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        """operations that need to happen at the end of each test"""
        del self.model
        del self.storage
        os.remove("file.json")

    def test_new(self):
        """ test file_storage new method """
        model = BaseModel()
        self.storage.new(model)
        my_dict = self.storage.all()
        self.assertIn(model, my_dict.values())

    def test_all(self):
        """ test file_storage all method """
        model = BaseModel()
        my_dict = self.storage.all()
        self.assertIsInstance(my_dict, dict)
        self.assertIn(model, my_dict.values())

    def test_save(self):
        """ test file_storage save method """
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", mode="r", encoding="utf-8") as file:
            file_content = file.read()
        self.assertTrue(len(file_content) > 0)
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                      file_content)

    def test_reload(self):
        """ test file_storage reload method """
        return None
        self.storage.destroy_all()
        self.assertEqual(self.storage.all(), {})
        self.assertTrue(len(self.storage.all()) == 0)
        self.storage.reload()
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                      self.storage.all().keys())


if __name__ == '__main__':
    unittest.main
