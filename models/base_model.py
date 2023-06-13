#!/usr/bin/python3
"""base model class"""

import uuid
from datetime import datetime


class BaseModel:
    """this class is the basis for other classes within the project.
    it holds all shared methods and attributes.
    """
    def __init__(self):
        """this is the first time you define __init__"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        return '[{}] ({}) {}'.format(
               self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj

    def __init__(self, *args, **kwargs):
        """this is the second time __init__ is defined.
        The way python works, it'll only take the latest definition,
        ignoring any earlier definitions.

        due to this, it will never run the code under the first definition.
        you can fix it by taking all your code from
        the first time you define __init__
        and moving it down here,
        so the one __init__ that Python runs has everything we need in it

        once that is done,
        please replace this documentation with an actual documentation
        or I can do that later, if you prefer.
        Jabulani
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(
                                   kwargs['created_at'],
                                   '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updat_at'] = datetime.strptime(
                                 kwargs['update_at'],
                                 '%Y-%m-%dT%H:%M:%S.%f')

        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
