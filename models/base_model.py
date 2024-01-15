#!/usr/bin/python3
"""
Module for the BaseModel class.
"""
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self,key, value)



    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()


    def to_dict(self):
         """Returns a dictionary representation of an instance."""

         my_dict = self.__dict__.copy()
         my_dict["__class__"] = self.__class__.__name__
         my_dict["created_at"] = self.created_at.isoformat()
         my_dict["updated_at"] = self.updated_at.isoformat()

         return my_dict
         
        
    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        my_class = self.__class__.__name__
        return "[{}] ({}) {}".format(my_class, self.id, self.__dict__)



if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


