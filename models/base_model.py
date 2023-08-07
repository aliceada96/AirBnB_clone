#!/usr/bin/python3


import uuid
import datetime


class BaseModel:
    def __init__(self):
        """Initialize an instance of the BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Print : [<class name>] (<self.id>) <self.__dict__>;"""
        return "[{}] ({}) {}".format(
             self.__class__.__name__, self.id, vars(self))

    def save(self):
        """Update the public instance attribute updated_at
        with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values
         of __dict__ of the instance:
        """
        self_dict = self.__dict__
        self_dict["__class__"] = self.__class__.__name__
        self_dict["created_at"] = self_dict["created_at"].isoformat()
        self_dict["updated_at"] = self_dict["updated_at"].isoformat()
        return self_dict
