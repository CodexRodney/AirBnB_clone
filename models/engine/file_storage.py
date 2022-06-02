#!/usr/bin/python3

"""
Defines a class FileStorage
"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return __objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key_name = str(type(obj).__name__) + str(obj.id)  # key name for the obj
        __objects[key_name] = obj

    def save(self):
        """
        Serializes objects to the JSON file in the path __file_path
        """
        with open(__file_path, 'w') as myFile:
            json.dump(__objects, myFile)

    def reload(self):
        """
        Deserializes the JSON file to __objects

        Only if the JSON file exists else do nothing. If file doesn't exist
        no exception should be raised
        """
        try:
            with open(__file_path) as myFile:
                __objects = json.load(myFile)
        except:
            return
