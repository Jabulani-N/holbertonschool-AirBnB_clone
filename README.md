# holbertonschool-AirBnB_clone
A repository that clones certain AirBnB functionality

<p align="left">

  <img src="https://stack.com.au/wp-content/uploads/2016/12/howard.jpg" width="400\"/>

<br>

# Task 0 - README, AUTHORS

create readme

create authors page

description and code examples of the command interpreter:

* how to start

* how to use

`AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository

# Task 2 - Unittest

unittests will be graded using `python3 -m unittest discover tests`

resource [from youtube](https://youtu.be/WFRljVPHrkE?t=180):

`with mock.patch('fileWheremethodIsUsed.method', return_value=mocked_return_value)`

## BaseModel tests (task 3)

* instanciation

* id

* creation times

* string override via print

* dicitonary creation via `to_dict()`

* * dictionary contains id, created_at, updated at

* * dictionary contains `__class__`

## BaseModel tests (task 4)

* test ability to create an instance when feeding it a dictionary

* * we can do this by using the `to_dict()` method already there.

* * * this way, we'll also already know the values each attirbute should be

## known issues

### SOLVED: unittest can find the test file, but fails to import the test module:

- `ImportError: Failed to import test module: test_models.test_base_model`

potential solutions:

* check names of everything within the file, and be sure it lines up exactly

Solution: I was using unitest wrong, and attempting to mock something while outside any class. I commented that out, and am reviewing how to properly use "with patch" to mock things.


# File Storage tests

Setup: creates a BaseModel instance to work with.

TearDown: deletes the instance created in setup.

# User tests

these tests ascertain attributes exist with the correct permissions

# amenity tests

these tests ascertain attributes exist with the correct permissions

# City tests

these tests ascertain attributes exist with the correct permissions

# Task 3 - BaseModel

`BaseModel` will be a class contained in `models/base_model.py`

public instance attributes:

* id - string

* created_at - datetime

* updated_at - datetime

## Tests - Task 3

test that attributes get properly set

- Jabulani: is committed to doing this

according to [this](https://stackoverflow.com/questions/16310989/python-how-to-unmock-reset-mock-during-testing), which get it's info from [this](https://docs.python.org/3/library/unittest.mock.html#patch) you can isolate your magicmocks via setUp:

```

p = patch("Channel.all", new=MagicMock(return_value=channel_list))

p.start()

```

and tearDown:

```

p.stop()

```