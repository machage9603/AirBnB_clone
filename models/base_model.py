#!/usr/bin/python3
"""Defines the BaseModel"""

from uuid import uuid4
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:  # If kwargs is not empty
            # Iterate over the key-value pairs in kwargs
            for key, value in kwargs.items():
                # Skip the '__class__' key
                if key == '__class__':
                    continue
                # If the key is 'created_at' or 'updated_at', convert the string to a datetime object
                elif key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    # Set other attributes using the key-value pairs
                    setattr(self, key, value)
        else:  # If kwargs is empty
            # Create new instance attributes 'id' and 'created_at'
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

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
