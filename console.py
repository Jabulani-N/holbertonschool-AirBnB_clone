#!/usr/bin/env python3
"""console module"""
import cmd
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class"""

    prompt = "(hbnb)"

    def do_create(self, args):
        """Function to create new BaseModel instance"""
        if not args:
            print("** class name missing **")
        elif args not in ["BaseModel"]:
            print("** class does not exist **")
        elif args == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_clear(self, args):
        """clears the console screen"""
        os.system("cls" if os.name == "nt" else "clear")

    def do_all(self, args):
        """function to print all instances"""
        classes = ["BaseModel"]
        all_objs = storage.all()
        if len(args) > 0:
            if args not in classes:
                print("** class doesn't exist **")
                return
            else:
                objs = [str(all_objs[k]) for k in all_objs if args in k]
        else:
            objs = [str(obj) for obj in all_objs.values()]
            print(objs)

        def do_update(self, args):
            """updates an instance based on class name and id"""
            args = args.split()
            classes = ["BaseModel"]
            all_objs = storage.all()
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                if args[0] not in classes:
                    print("** class doesn't exsist **")
                else:
                    print("** instance id missing **")
                elif len(args) == 2:
                    key = args[0] + "." = args[1]
                    if key  not in all_objs:
                        print("** no instance found **")
                    else:
                        print("** attribute name missing **")
                elif len(args) == 3:
                    key = args[0] + "." = args[1]
                    if key not in all_objs:
                        print("** no instance found **")
                    elif args[2] in ["id", "created_at", "update_at"]:
                        print("** can't update attribute **")
                    else:
                        print("** value missing **")
