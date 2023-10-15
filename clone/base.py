#!/usr/bin/python3
"""This module contains BaseModel class"""

from uuid import uuid4
from datetime import datetime
from __init__ import storage


class BaseModel():
    """The Base model class"""

    def __init__(self):
        """initializing base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update public attribute with the cuttent date time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """create a dict """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()

        return dict_obj

    def __str__(self):
        """Magic method that define human readable of BaseModel object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.to_dict())
