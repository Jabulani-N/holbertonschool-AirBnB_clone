#!/usr/bin/python3
"""this class reviews"""

from models.base_model import BaseModel

class Review(BaseModel):
    """class that reviews"""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
