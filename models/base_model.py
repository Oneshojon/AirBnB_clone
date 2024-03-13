#!/usr/bin/python3
"Defines all common attributes/methods for other classes."
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    A class to represent AirBnB_clone.

    Attributes:
        to_dict(self)
        __save(self)
        __str__(self)

    """
    def __init__(self, *args, **kwargs):
        """
        Constructor that initializes a new instance.
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance

        Aggs:
            None

        Returns:
            dict: A dictionary representatation of the class.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, id, and all instance
            attributes and their values
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self__dict__))
