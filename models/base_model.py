#!/usr/bin/python3
"""Base model Class for Homecooker"""

from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class BaseModel():
    """ Class that functions as a model for the other classes."""
    id = Column(String(60), primary_key=True)
    created_at = Column(Datetime, default=datetime.utcnow)
    updated_at = Column(Datetime, default=datetime.utcnow)

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""
    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if not self.id:
                setattr(self, 'id', str(uuid.uuid4()))
            if not self.created_at:
                self.created_at = datetime.now()
            if not self.updated_at:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """----------"""
    """- Public -"""
    """----------"""
    def delete(self):
        """Delete de current instance from storage."""
        models.storage.delete(self)

    def save(self):
        """Updates the attribute 'updated_at' and saves the instance."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation containing all key: values of
        the instance."""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    """-----------"""
    """- Private -"""
    """-----------"""

    def __str__(self):
        """The string representation of the BaseModel class."""
        return ("[{}]({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    """-----------"""
    """- Class ---"""
    """-----------"""

    """-----------"""
    """- Static --"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
