#!/usr/bin/python3
"""File Storage Class"""


import json
from ...models.base_model import BaseModel
from ...models.state import State
from ...models.city import City
from ...models.amenity import Amenity
from ...models.place import Place
from ...models.review import Review
from ...models.user import User


class FileStorage:
    """
    This class provides a file storage module for serializing instances
    to a JSON file and deserializing JSON files to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: A dictionary containing all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
            obj: The object to be added.
        """
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        Serializes the objects dictionary to a JSON file.
        The JSON file path is specified by self.__file_path.
        """
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file and updates the objects dictionary.
        """
        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
            'User': User
        }

        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            # Handle case where file doesn't exist
            pass
