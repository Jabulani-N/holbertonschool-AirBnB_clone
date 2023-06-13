"""testing module using unittest
This module exclusively tests the BaseModel class
"""


import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
import io
import sys

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

    def tearDown(self):
        print("Base tearDown")

    # first test cluster: public attributes
    # self.assertEqual(thing, what_thing_should_equal_to_pass_test)
    def test_instanciation(self):
        """ascertain instance created with attributes
        and that attributes are correct type
        """

        newbase1 = BaseModel()
        self.assertIsInstance(newbase1.id, str)
        self.assertIsInstance(newbase1.created_at, datetime.datetime)
        # check to make sure the update time instanciated correctly
        # by being the same as the created time
        self.assertEqual(newbase1.created_at, newbase1.updated_at)

        # lines below are attemps to verify the datetime returned is correct
        # they are commented out for now, to be returned to later
        # with mock.patch('models.base_model.datetime.utcnow()', \
        # return_value=datetime(2035, 1, 1, 13, 45, 6, 789)):
        #    # mock datetime to make all uses of datetime.utcnow
        #    # return a constant date
        #   pass

    def test_unique_ID(self):
        """assures ID values created are not the same"""
        newBase1 = BaseModel()
        newBase2 = BaseModel()
        newBase3 = BaseModel()
        self.assertNotEqual(newBase1.id, BaseModel().id)
        self.assertNotEqual(newBase1.id, newBase2.id)
        self.assertNotEqual(newBase1.id, newBase3.id)
        self.assertNotEqual(newBase2.id, newBase3.id)

    def test_updatetime(self):
        """assures update changes the updatetime
        by asserting difference from time created
        """
        newBase1 = BaseModel()
        starting_time_created = newBase1.created_at
        newBase1.save()
        self.assertNotEqual(starting_time_created, newBase1.updated_at)

    def test_str_override(self):
        """assures the override for __str__ returns
        using the correct formatting characters
        """
        newBase1 = BaseModel()
        capturedOutput = io.StringIO()
        # created StringIO object
        sys.stdout = capturedOutput
        # redirected stdout to that object
        print(newBase1)
        sys.stdout = sys.__stdout__
        # put stdout back to where it belongs
        # before making sure it actually gave the needed brackets
        self.assertIsInstance(capturedOutput.getvalue())
        # the above test makes sure it works at all
        # if it fails there, we'll have a more accurate knowledge
        # than if it failed only to contain the necessary chars
        self.assertTrue('[' in capturedOutput.getvalue())
        self.assertTrue(']' in capturedOutput.getvalue())
        self.assertTrue('(' in capturedOutput.getvalue())
        self.assertTrue(')' in capturedOutput.getvalue())
        # we are assuming they were used correctly
        # if all characters are used


    def test_dictionary_created(self):
        """ensures a dictionary is returned
        when using instance.to_dict()
        """
        newBase1 = BaseModel()
        self.assertIsInstance(newBase1.to_dict(), dict)

    def test_dictionary_keys(self):
        """tests to assure required keys contain something"""
        newBase1 = BaseModel()
        madeDict = newBase1.to_dict()
        self.assertIsInstance(madeDict["id"], str)
        self.assertIsInstance(madeDict["created_at"], str)
        self.assertIsInstance(madeDict["updated_at"], str)
        # specifications required dateteimes be formatted into str
        self.assertNotEqual(madeDict['__class__'], None)

    def test_instanciation_from_dict(self):
        """test's class's ability to initialize via dictionary
        uses class's own to_dict() method to created the dicitonary
        """
        newBase1 = BaseModel()
        base1Dict = newBase1.to_dict()
        newBase2 = BaseModel(base1Dict)
        self.assertIsInstance(newBase2, BaseModel)
        self.assertEqual(newBase1.id, newBase2.id)
        self.assertEqual(newBase1.created_at, newBase2.created_at)
        self.assertEqual(newBase1.updated_at, newBase2.updated_at)



if __name__ == '__main__':
    unittest.main
