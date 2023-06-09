"""testing module using unittest
This module exclusively tests the BaseModel class
"""


import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """tests class for class BaseModel.
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation

    you'll probably want to mock a known datetime value to put into this
    """

    #first test cluster: public attributes
    # self.assertEqual(thing, what_thing_should_equal_to_pass_test)
    def test_instanciation(self):
        newbase1 = BaseModel()
        self.assertEqual(type(newbase1.id), str)


if __name__ == '__main__':
    unittest.main
