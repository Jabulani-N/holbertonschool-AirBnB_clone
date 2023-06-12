#!/usr/bin/python3
"""this class gets good"""


import json

class FileStorage:
    """this class just works:"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        try:
            with