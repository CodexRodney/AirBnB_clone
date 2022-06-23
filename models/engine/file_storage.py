#!/usr/bin/python3

"""
Defines a class FileStorage
"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    # string- Path to the JSON file
    __file_path = "file.json"
    # Dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key_name = str(type(obj).__name__) + '.' +  str(obj.id)
        type(self).__objects[key_name] = obj

    def save(self):
        """
        Serializes objects to the JSON file in the path __file_path
        """
        obj_dict = {}
        for key, obj in type(self).__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(type(self).__file_path, 'w') as myFile:
            json.dump(obj_dict, myFile)

    def reload(self):
        """
        Deserializes the JSON file to __objects

        Only if the JSON file exists else do nothing. If file doesn't exist
        no exception should be raised
        """
        try:
            with open(type(self).__file_path) as myFile:
                json_dict = json.load(myFile)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except:
            pass
