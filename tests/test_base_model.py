"""testing module using unittest
This module exclusively tests the BaseModel class
"""


import unittest
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel

# items below are imported for unittest.mock
import uuid
from datetime import datetime

datetime.utcnow = MagicMock(retrurn_value="return goes here")
# Datetime note:
# datetime.datetime(2012, 1, 1, 10, 10, 10)
# seems to create and return a class instance

# the instance has attributes that can be called

# for testing, we can mock to crete this class,
# and check an identical one was created.

class TestBaseModel(unittest.TestCase):
    """tests class for class BaseModel.
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation

    you'll probably want to mock a known datetime value to put into this
    """

    def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Base setUp")
        p = patch("Channel.all", new=MagicMock(return_value=channel_list))
        p.start()


    def tearDown(self):
        print("Base tearDown")
        p.stop()  # defined in setUp

    #first test cluster: public attributes
    # self.assertEqual(thing, what_thing_should_equal_to_pass_test)
    def test_instanciation(self):
        newbase1 = BaseModel()
        self.assertEqual(type(newbase1.id), str)


if __name__ == '__main__':
    unittest.main
