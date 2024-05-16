#!/usr/bin/python3

"""Defines the HBnB console"""

import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime
from shlex import shlex


class HBNBCommand(cmd.Cmd):
    """Hbnb shell"""
    prompt = '(hbnb) '
    clslist = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        'User': User
    }

    def emptyline(self):
        """Handle empty lines."""
        pass

    def do_create(self, class_name):
        """Creates a new instance of a class and prints its id."""
        class_name = class_name.strip()
        if class_name not in self.clslist:
            print('** class does not exist **')
        else:
            obj = self.clslist[class_name]()
            models.storage.save()
            print(obj.id)

    def do_show(self, args):
        """Show instance based on id."""
        class_name, obj_id = args.split()
        if class_name not in self.clslist:
            print("** class doesn't exist **")
        else:
            k = f"{class_name}.{obj_id}"
            obj = models.storage.all().get(k)
            if obj:
                print(obj)
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """Destroy instance based on id."""
        class_name, object_id = arg.split()
        key = f"{class_name}.{object_id}"
        if class_name not in self.clslist:
            print("** class doesn't exist **")
        elif key not in models.storage.all():
            print('** no instance found **')
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, clsname):
        """Prints all instances based on class name."""
        clsname = clsname.strip()
        if clsname not in self.clslist:
            return False
        instances = [str(v) for v in models.storage.all().values()
                     if isinstance(v, self.clslist[clsname])]
        print(*instances, sep='\n')

    def do_update(self, arg):
        """Updates an instance using class name, id, attribute name, and value."""
        clsname, objid, attrname, attrvalue = arg.split()
        k = f"{clsname}.{objid}"
        obj = models.storage.all().get(k)
        if not obj:
            print('** no instance found **')
        else:
            setattr(obj, attrname, attrvalue)
            obj.updated_at = datetime.now()
            models.storage.save()
