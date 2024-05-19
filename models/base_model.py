#!/usr/bin/python3
"""Defines the BaseModel class."""


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initializes a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attributeupdated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary containing values of __dict__ of the instance."""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
