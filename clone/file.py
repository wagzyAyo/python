import json


class FileStorage():
    """Serializes instance to json file and deserilizes json file to instance"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets __object"""

    def save(self):
        """serializes object to a json file"""
        self.__objects = json.dumps(self.__objects)
        return self.__objects

    def reload(self):
        """deseializes json object"""
        if self.__file_path:
            self.__dict__ = json.loads(self.__objects)
        else:
            pass
