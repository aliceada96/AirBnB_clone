#!/usr/bin/python3
import json

class FileStorage:
    """serialize instances to a JSON file and deserializes JSON
    file to instances: """

    __file_path = "file.json"
    __objects = {}

    #def __init__(self, filename):
    def all(self):
        """return list of objects in storage."""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
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
        """serializes __objects to the JSON file"""
        with open(self.__file_path,"w", encoding="utf-8") as f:
            json.dump(self.__objects, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:

            with open(self.__file_path,"r", encoding="utf-8") as f:
                from_json = json.load(f)
                if from_json is None:#empty file
                    pass#do nothing
                else:
                    self.__objects.update(from_json)
        except FileNotFoundError:
            pass
