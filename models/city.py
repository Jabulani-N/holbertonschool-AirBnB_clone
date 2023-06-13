#!/usr/bin/python3
"""the class this City deserves"""

from models.base_model import BaseModel

class City(BaseModel):
    """not the class this City needs right now"""
    state_id = ""
    name = ""

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)