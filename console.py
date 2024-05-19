#!/usr/bin/python3
"""Defines the console."""


import sys
import json
from models.base_model import BaseModel  


def load_data():
    try:
        with open("file.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("file.json", "w") as file:
        json.dump(data, file)

def create_command(args):
    if len(args) < 2:
        print("** class name missing **")
        return
    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return
    instance = globals()[class_name]()
    instance.save()
    print(instance.id)

def show_command(args):
    if len(args) < 3:
        print("** instance id missing **")
        return
    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return
    object_id = args[2]
    data = load_data()
    key = class_name + "." + object_id
    if key not in data:
        print("** no instance found **")
        return
    print(data[key])

def destroy_command(args):
    if len(args) < 3:
        print("** instance id missing **")
        return
    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return
    object_id = args[2]
    data = load_data()
    key = class_name + "." + object_id
    if key not in data:
        print("** no instance found **")
        return
    del data[key]
    save_data(data)

def all_command(args):
    data = load_data()
    if len(args) < 2:
        print([str(value) for value in data.values()])
        return
    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return
    print([str(value) for key, value in data.items() if key.startswith(class_name)])

def update_command(args):
    if len(args) < 5:
        print("** attribute name missing **")
        return
    class_name = args[1]
    if class_name not in globals():
        print("** class doesn't exist **")
        return
    object_id = args[2]
    data = load_data()
    key = class_name + "." + object_id
    if key not in data:
        print("** no instance found **")
        return
    attribute_name = args[3]
    if len(args) < 6:
        print("** value missing **")
        return
    attribute_value_str = args[4]
    # Assuming simple arguments: string, integer, and float
    try:
        attribute_value = eval(attribute_value_str)  # Convert string representation to appropriate type
    except (NameError, SyntaxError, ValueError):
        print("** invalid value **")
        return
    instance = globals()[class_name](**data[key])  # Reconstruct instance
    setattr(instance, attribute_name, attribute_value)  # Set attribute value
    instance.save()  # Save changes

def main():
    commands = {
        "create": create_command,
        "show": show_command,
        "destroy": destroy_command,
        "all": all_command,
        "update": update_command
    }
    if len(sys.argv) < 2:
        return
    command = sys.argv[1]
    if command not in commands:
        print("** command not found **")
        return
    commands[command](sys.argv)

if __name__ == "__main__":
    main()
