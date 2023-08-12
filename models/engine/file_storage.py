#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json


class FileStorage:
    """Serialize and deserialize instances to and from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    # def __init__(self, filename):
    def all(self):
        """Return a dictionary of all objects in storage.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Set an object in __objects with a key of <obj class name>.id.

        Args:
            obj (object): The object to be stored.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        value = obj.to_dict()
        self.__objects[key] = value

        """if not isinstance(obj, object) or \
        (not hasattr(obj,'save') and
         not hasattr(obj, 'load')):
            raise TypeError("object must have save() method")
        idnum = len(self.__objects)+1
        obj._id=str(idnum).zfill(4)
        print('new', type(obj), obj._id )
        self.__objects[obj] = {'type': str(type(obj)),
                               '_id' :  obj._id}
        with open(FileStorage.__file_path,"w+") as f:
            json.dump([o for o,_i in sorted(
                [(v['type'], v['_id'])
                 for k,v
                 in self.__objects.items()], key=lambda x:-x[-2])],f,)
            return True"""

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:

            with open(self.__file_path, "r", encoding="utf-8") as f:
                from_json = json.load(f)
                if from_json is None:  # empty file
                    pass  # do nothing
                else:
                    self.__objects.update(from_json)
        except FileNotFoundError:
            pass
