#!/usr/bin/python3
"""Defines the storage mechanism based on JSON
"""

import json
import models
from models.user import User
from models.recipe import Recipe
from models.review import Review
from hashlib import md5

classes = {"User": User, "Recipe": Recipe, "Review": Review}


class JStorage():
    """Object for MySQL interacion
    """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""
    __file_path = "data.json"
    __objects = {}

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """----------"""
    """- Public -"""
    """----------"""

    def all(self, cls=None):
        """ Select all elements of a class.
        if cls is None, returns a dictionary with all the elements of all
        classes; if cls is diferent from None, returns a dictionary with all
        elements of a specific class.
        """
        if cls is not None:
            ret_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    ret_dict[key] = value
            return ret_dict
        return self.__objects

    # -------------------------------------------------------------------------

    def close(self):
        """Uses the remove method on the session attribute.
        Returns nothing.
        """
        self.reload()

    # -------------------------------------------------------------------------

    def count(self, cls=None):
        """Counts the number of elements in the database.
        If cls is None, counts all elements regardless of the class.
        If cls is different from None, counts all elements in the specified
        class.
        Returns the number of elements counted.
        """
        all_classes = classes.values()
        if cls:
            counter = len(models.storage.all(cls).values())

        else:
            counter = 0
            for element in all_classes:
                counter += len(models.storage.all(element).values())

        return counter

    # -------------------------------------------------------------------------

    def delete(self, obj=None):
        """Deletes an element from the database.
        Only works if obj is different from None.
        Returns nothing.
        """
        if obj:
            self.__session.delete(obj)

    # -------------------------------------------------------------------------

    def get(self, cls, id):
        """Search for an object using its class and id.
        Returns the object matching the class and id given by cls and id
        respectively.
        Returns None if the object is not found.
        """
        if cls not in classes.values():
            return None

        all_of_class = models.storage.all(cls)
        for item in all_of_class.values():
            if item.id == id:
                return item

        return None

    # -------------------------------------------------------------------------

    def new(self, obj):
        """Adds the object to the database session.
        Returns nothing.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    # -------------------------------------------------------------------------

    def save(self):
        """Save changes to the current session.
        Returns nothing.
        """
        json_dict = {}
        for key in self.__objects:
            if key == "password":
                json_dict[key].decode()
            json_dict[key] = self.__objects[key].to_dict(code=1)

        with open(self.__file_path, 'w') as jfile:
            json.dump(json_dict, jfile)

    # -------------------------------------------------------------------------

    def reload(self):
        """Reload data from the database.
        Returns nothing.
        """
        try:
            with open(self.__file_path, 'r') as jfile:
                json_dict = json.load(jfile)
            for key in json_dict:
                self.__objects[key] =
                classes[json_dict[key]["__class__"]](**json_dict[key])
        except:
            pass
    # -------------------------------------------------------------------------

    """-----------"""
    """- Private -"""
    """-----------"""

    """-----------"""
    """- Class ---"""
    """-----------"""

    """-----------"""
    """- Static --"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
