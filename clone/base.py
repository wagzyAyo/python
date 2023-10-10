from uuid import uuid4
from datetime import datetime


class BaseModel():

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return "{} {} {}".format(class_name, (self.id))
