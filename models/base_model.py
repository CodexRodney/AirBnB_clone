#!/usr/bin/python3
"""
Defines a class BaseModel
"""


from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiates values to attributes
        """
        if kwargs:
            for key, item in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(item)
                    continue
                if key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(item)
                    continue
                self.__dict__[key] = item
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints [<class name>] (<self.id>) <self.__dict__>]
        """
        str1 = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return str1

    def save(self):
        """
        Updates attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        self.__dict__["__class__"] = type(self).__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
