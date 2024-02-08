#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances.
"""
import json
from model.base_model import BaseModel


class FileStorage:
    """
    instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel" : BaseModel}

    def all(self):
        """
        returns the dictionary __objects.
        """
         return self.__objects

     def new(self, obj):
         """
         sets in __objects the obj with key <obj class name>.id
         """
         if obj:
             key = "{}.{}".format(obj.__class__.__name__, obj.id)
             self.__objects[key] = obj

    def save(self):
        """save/serializes obj dictionaries to json file"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the json file to obbjects.
        """
        try:
            with open(FileStorage.__file_path) as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dic.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
            except FileNotFoundError:
                pass
