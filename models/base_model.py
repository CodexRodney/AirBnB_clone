#!/usr/bin/python3
"""
Defines a class BaseModel
"""


import datetime
import uuid

class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        Instantiates values to attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Prints [<class name>] (<self.id>) <self.__dict__>]
        """
        str1 = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return str1

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        self.__dict__["__class__"] = type(self).__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
