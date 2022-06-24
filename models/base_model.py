#!/usr/bin/python3
"""
Defines a class BaseModel
"""


from datetime import datetime
import uuid
import models


time = "%Y-%m-%dT%H:%M:%S.%f"


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
                    self.__dict__[key] = datetime.strptime(item, time)
                    continue
                if key == "updated_at":
                    self.__dict__[key] = datetime.strptime(item, time)
                    continue
                self.__dict__[key] = item
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
