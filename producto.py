import json
import uuid

class Producto:
    def __init__(self,name):
        self.order_id = ''
        self.name = name


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)
    def __str__(self):
        return json.dumps(self.__dict__)