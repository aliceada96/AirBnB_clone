#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        # value = obj.to_dict() Is the below correct
        value = obj
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
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
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
            with open(self.__file_path, "r", encoding="utf-8") as f:
                from_json = json.load(f)
                if from_json is None:  # empty file
                    pass  # do nothing
                else:
                    for key, value in from_json.items():
                        class_name = value['__class__']
                        if class_name in classes:
                            instance_class = classes[class_name]
                            instance = instance_class(**value)
                            self.__objects[key] = instance
        except FileNotFoundError:
            pass
