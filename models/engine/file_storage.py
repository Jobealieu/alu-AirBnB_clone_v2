#!/usr/bin/python3
"""FileStorage module for serializing and deserializing objects to JSON."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class FileStorage:
    """Handles serialization and deserialization of objects to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary __objects, filtered by cls if provided."""
        if cls is not None:
            return {
                key: obj
                for key, obj in self.__objects.items()
                if cls.__name__ == obj.__class__.__name__
            }
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = '{}.{}'.format(obj.to_dict()["__class__"], obj.to_dict()["id"])
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        json_objects = {}
        for key in self.__objects.keys():
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key in obj_dict:
                    cls_name = obj_dict[key]["__class__"]
                    self.__objects[key] = classes[cls_name](**obj_dict[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if not None."""
        if obj is not None:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if obj_key in self.__objects:
                del self.__objects[obj_key]
                self.save()

    def close(self):
        """Call reload to deserialize the JSON file to objects."""
        self.reload()
