#!/usr/bin/python3
"""this class is about the user"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
