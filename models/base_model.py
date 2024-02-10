#!/usr/bin/python3
"""
Defines the base model
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        String representation when instance is printed
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        self.__dict__.update({'updated_at': datetime.now()})
        models.storage.save(self)

    def to_dict(self):
        rdict = dict(self.__dict__)
        rdict["created_at"] = self.created_at.isformat()
        rdict["updated_at"] = self.updated_at.isformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
