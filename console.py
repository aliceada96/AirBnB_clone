#!/usr/bin/python3
"""This module implements a simple command interpreter for AirBnB program.
"""
import cmd

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

"""

"""
class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter.

    Args:
        cmd (module): extends the functionality of the cmd module

    Returns:
        _type_: _description_
    """
    prompt = "(hbnb) "
    classes = {"BaseModel",
               "Users",
               }

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program.
        """
        return True
    
    def emptyline(self) -> bool:
        # return super().emptyline()
        pass

    def do_create(self, arg):
        """Create an object from the model specified by its class."""
        if not arg or len(arg) == 0:
            print('** class name missing **')
            return
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Print the string representation of an instance.
        Representation is based on the class name and id.

        Args:
            args (str): a string containing args separated by spaces.
        """
        args = args.split()
        if not args or len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print('** no instance found **')
            return
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id.
        (save the change into the JSON file)

        Args:
            args (str): a string containing args separated by spaces.
        """
        args = args.split()
        if not args or len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print('** no instance found **')
            return
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """Print all string representation of all instances.
        Representation is based or not on the class name. 

        Args:
            args (str): a string containing args separated by spaces.
        """
        args = args.split()
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        list_of_instances = []
        for i in storage.all().values():
            list_of_instances.append(BaseModel(**i).__str__())
        print(list_of_instances)

    def do_update(self, args):
        """Print all string representation of all instances
        Represenation is based or not on the class name. 

        Args:
            args (str): a string containing args separated by spaces.
        """
        args = args.split()
        if not args or len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print('** instance id missing **')
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print('** no instance found **')
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        elif args[2] in ["created_at", "updated_at", "id"]:
            return
        else:
            key = args[2]
            value = args[3] # TODO probably should do eval() here
            storage.all()["{}.{}".format(args[0], args[1])][key] = value
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
