#!/usr/bin/python3
"""this module gets good"""


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
        new_dict = {}
        for key in FileStorage. __objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.load(f)
            for key in json_dict:
                class_name, obj_id = key.split('.')
            if class_name = "BaseModel"
                module = __import__('models.base_model', fromlist=
                [class_name])
                obj_cls = getattr(module, class_name)
                obj = obj_cls(**json_dict[key])
                FileStorage.__objects[key] = obj
            except FileNotFoundError:
                pass
