#!/usr/bin/python3
"""this class does stately things"""

from models.base_model import BaseModel

class State(BaseModel):
    """I am in a State of distress"""
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)