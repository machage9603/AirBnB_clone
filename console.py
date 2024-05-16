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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        clsname = arg.strip()  # Remove leading/trailing whitespace
        if not clsname:
            print('** class name missing **')
        elif clsname not in self.clslist:
            print('** class doesn\'t exist **')
        else:
            obj = self.clslist[clsname]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Show instance based on id."""
        clsname, objid = None, None
        args = arg.split()
        if len(args) > 0:
            clsname = args[0].strip()
        if len(args) > 1:
            objid = args[1].strip()
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif clsname not in self.clslist:
            print("** class doesn't exist **")
        else:
            k = f"{clsname}.{objid}"
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """Destroy instance based on id."""
        clsname, objid = None, None
        args = arg.split()
        if len(args) > 0:
            clsname = args[0].strip()
        if len(args) > 1:
            objid = args[1].strip()
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif clsname not in self.clslist:
            print("** class doesn't exist **")
        else:
            k = f"{clsname}.{objid}"
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class name."""
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            clsname = arg.strip()
            if clsname not in self.clslist:
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.clslist[clsname]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        clsname, objid, attrname, attrval = None, None, None, None
        updatetime = datetime.now()
        args = shlex.split(arg)  # Use shlex for better argument parsing
        if len(args) > 0:
            clsname = args[0].strip()
        if len(args) > 1:
            objid = args[1].strip()
        if len(args) > 2:
            attrname = args[2].strip()
        if len(args) > 3:
            attrval = args
