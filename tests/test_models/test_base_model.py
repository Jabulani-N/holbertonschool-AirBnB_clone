"""testing module using unittest
This module exclusively tests the BaseModel class
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel

# items below are imported for unittest.mock
import uuid
import datetime

# datetime.datetime(year, month, day, hour, minute, second, microsecond)

# Datetime note:
# datetime.datetime(2012, 1, 1, 10, 10, 10)
# creates and returns a class instance

# the instance has attributes that can be called
# the instance also returns a formatted representation when you use
# `print(that_instance)`

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
        # p = patch("Channel.all", new=MagicMock(return_value=channel_list))
        # p.start()

    def tearDown(self):
        print("Base tearDown")
        # p.stop()
        # p is defined in setUp

    # first test cluster: public attributes
    # self.assertEqual(thing, what_thing_should_equal_to_pass_test)
    def test_instanciation(self):
        # ascertain instance created with attributes
        # and that attributes are correct type
        newbase1 = BaseModel()
        self.assertIsInstance(newbase1.id, str)
        self.assertIsInstance(newbase1.created_at, datetime.datetime)

        # lines below are attemps to verify the datetime returned is correct
        # they are commented out for now, to be returned to later
        # with mock.patch('models.base_model.datetime.utcnow()', \
        # return_value=datetime(2035, 1, 1, 13, 45, 6, 789)):
        #    # mock datetime to make all uses of datetime.utcnow
        #    # return a constant date
        #   pass


if __name__ == '__main__':
    unittest.main
