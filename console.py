#!/usr/bin/python3

"""
Defines a class HBNBCommand(cmd.Cmd)
"""

import cmd
from models.base_model import BaseModel
from models.user import User
import models


classes = {"User": User, "BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """
        Used to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        Creates a new instance of a class, saves it(to the JSON file)
        and prints the id
        """
        if line:
            if line not in classes:
                print("** class doesn't exist **")
            else:
                obj = classes[line]()
                obj.save()
                print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif not args[0].strip() in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0].strip(), args[1].strip())
            objs = models.storage.all()
            if key in models.storage.all():
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id and saves the changes to JSON File
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif not args[0].strip() in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0].strip(), args[1].strip())
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not the class name
        """
        args = line.split()
        # empty list but will store string representation of objects
        list_objs = []
        if len(args) == 0 or args[0].strip() in classes:
            for obj in models.storage.all().keys():
                list_objs.append(str(models.storage.all()[obj]))
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute and saves the changes
        into the JSON file
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif not args[0].strip() in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0].strip(), args[1].strip())
            if key in models.storage.all():
                models.storage.all()[key].__dict__[args[2]] = args[3]
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
