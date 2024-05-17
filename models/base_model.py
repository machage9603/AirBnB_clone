#!/usr/bin/python3
"""Defines the BaseModel"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the print representation of the BaseModel class"""
        return "{} ({})".format(type(self).__name__, self.id)

    def save(self):
        """Update updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__':
                        (str(type(self)).split('.')[-1]).split('\'')[0]})
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
