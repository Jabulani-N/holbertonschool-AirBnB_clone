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

# Task 3 - BaseModel

`BaseModel` will be a class contained in `models/base_model.py`

public instance attributes:

* id - string

* created_at - datetime

* updated_at - datetime

## Tests - Task 3

test that attributes get properly set

- Jabulani: is committed to doing it

according to [this](https://stackoverflow.com/questions/16310989/python-how-to-unmock-reset-mock-during-testing) you can isolate your magicmocks via startup having

```

p = patch("Channel.all", new=MagicMock(return_value=channel_list))

p.start()

```

and teardown having

```

p.stop()

```