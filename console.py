#!/usr/bin/python3
"""This module implements a simple command interpreter for AirBnB program."""

import cmd
import re
import shlex
import json

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter for the AirBnB program.

    Attributes:
        prompt (str): The command prompt.
        classes (set): A set of available class names.
    """

    prompt = "(hbnb) "
    classes = {"BaseModel",
               "User",
               "State",
               "City",
               "Place",
               "Review",
               "Amenity",
               }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program."""
        print()
        return True

    def emptyline(self) -> bool:
        """Do nothing on an empty line.

        It Overrides emptyline() method from cmd.Cmd.
        """
        # return super().emptyline()
        pass

    def do_create(self, arg):
        """Create an object from the specified class.

        Args:
            arg (str): The class name.
        """
        if not arg or len(arg) == 0:  # TO BE CHECKED
            print("** class name missing **")
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
        Usage: show <Classname> <instance id>.

        Args:
            args (str): a string containing class name and id.
        """
        args = args.split()
        if not args or len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id.

        (save the change into the JSON file)

        Args:
            args (str): a string containing class name and id.
        Retuns:
            None
        """
        args = args.split()
        if not args or len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, args):
        """Print all string representation of all instances.

        Representation is based or not on the class name.

        Args:
            args (str): a string containing a class name.
        Returns:
            None
        """
        args = args.split()
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        list_of_instances = []
        for i in storage.all().values():
            list_of_instances.append(i.__str__())
        print(list_of_instances)

    def do_count(self, args):
        """Print number of objects from class.

        Args:
            args (str): a string containing a class name.

        Returns:
            None
        """
        args = args.split()
        if not args or len(args) != 1:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            instances = 0
            for i in storage.all().values():
                if args[0] == i["__class__"]:
                    instances += 1
            print(instances)

    def do_update(self, args):
        """Update an instance based on the class name and id.

         Updates by adding or updating attribute (save change into JSON file.
        Representation is based or not on the class name.

        Args:
            args (str): a string containing
             class name, id, attribute key and value.
        Returns:
            None
        """
        args = shlex.split(args)  # .split()
        if not args or len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
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
            value = args[3]
            instance_key = "{}.{}".format(args[0], args[1])
            instance = storage.all()[instance_key]

            # check if the input has a dictionary from the 3rd command
            x = "".join(args[2:])
            if x.startswith("{") and x.endswith("}"):
                # convert the 3rd command from str to dict and iterate
                try:
                    update_dict = json.loads(x)
                    for k, v in update_dict.items():
                        setattr(instance, k, v)
                except json.JSONDecodeError:
                    print("Invalid Json format")
                    return
            else:
                # no dictionary - standard format.
                setattr(instance, key, value)
                instance.save()

    def default(self, line: str) -> None:
        """Call on an input line when the command prefix is not recognized.

        If this method is not overridden, it prints an error message and
        returns.

        Args:
            line (str): sting of commands in a non-standard format

        Returns:
            str: calls the corresponding command the standard format
        """
        calls = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }

        if "." not in line:
            print("** Unknown syntax: {}\n".format(line))
            return False
        else:
            args = line.split(".", maxsplit=1)
            # split the second arg at '(',')', and ','
            others = re.split(r"[)(,]", args[1])
            # remove spaces in the result elements
            others = [i.strip() for i in others]
            command = others[0]
            string = args[0] + " " + " ".join(others[1:])
            if command in calls.keys():
                return calls[others[0]](string)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
    # print("") # TODO will this be valid for all exits
