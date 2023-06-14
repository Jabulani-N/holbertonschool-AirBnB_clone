#!/usr/bin/env python3
"""
Entry point for the command interpreter
"""
import cmd
from models import storage
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """quits"""
        return True

    def do_quit(self, line):
        """quits"""
        return True

    def do_create(self, arg):
        """Creates a new instance of whatever class you tell it
        be sure to import the class to this module
        in order to be able to create an instance
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            # print(arg)
            new_obj = eval(arg + "('Test')")
            new_obj.save()
            print(new_obj.id)
        except Exception as e:
            print(e)
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg or len(args) != 2:
            print("** class name missing **")
            return
        try:
            storage.reload()
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            print(obj)
        except KeyError:
            print("** no instance found **")
        except (NameError, SyntaxError):
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance of a class"""
        args = arg.split()
        if not arg or len(args) != 2:
            print("** class name missing **")
            return
        try:
            storage.reload()
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except (NameError, SyntaxError):
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all instances of a class"""
        args = arg.split()
        objs = storage.all()
        if args and args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if not args:
            print([str(objs[obj]) for obj in objs])
        else:
           # print([str(objs[obj]) for obj
           pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
