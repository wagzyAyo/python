import json
import os


class FileStorage():
    """Serializes instance to json file and deserilizes json file to instance"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets __object with new object"""
        key = f"{__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes object to a json file"""
        ser_obj = {key: value.to_dict()
                   for key, value in self.__objects.items()}
        with open(file=self.__file_path, mode='w') as file:
            json.dump(ser_obj, file)

    def reload(self):
        """deseializes json file to python object"""
        if os.path.exists("file.json"):
            with open("file.json", mode='r') as file:
                data = json.load(file)
                return data
        else:
            pass
