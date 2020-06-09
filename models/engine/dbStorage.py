#!/usr/bin/python3
"""Defines the storage mechanism based on MySQL
"""

import models
from models.user import User
from models.recipe import Recipe
from models.review import Review
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Recipe": Recipe, "Review": Review}


class DbStorage():
    """Object for MySQL interacion
    """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the class.
        """
        HC_MYSQL_USER = getenv('HC_MYSQL_USER')
        HC_MYSQL_PWD = getenv('HC_MYSQL_PWD')
        HC_MYSQL_HOST = getenv('HC_MYSQL_HOST')
        HC_MYSQL_DB = getenv('HC_MYSQL_DB')
        HC_ENV = getenv('HC_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HC_MYSQL_USER,
                                             HC_MYSQL_PWD,
                                             HC_MySQL_HOST,
                                             HC_MySQL_DB))
        if HC_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

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
        class_dict = {}
        for element in classes:

            if cls is None or cls is classes[clss] or cls is clss:
                objects = self.session.query(classes[clss]).all()

                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    class_dict[key] = obj

        return class_dict

    # -------------------------------------------------------------------------

    def close(self):
        """Uses the remove method on the session attribute.
        Returns nothing.
        """
        self.__session.remove()

    # -------------------------------------------------------------------------

    def count(self, cls=None):
        """Counts the number of elements in the database.
        If cls is None, counts all elements regardless of the class.
        If cls is different from None, counts all elements in the specified
        class.
        Returns the number of elements counted.
        """
        every_class = classes.values()
        if cls:
            count = len(models.storage.all(cls).values())

        else:
            count = 0
            for index in every_class:
                count += len(models.storage.all(index).values())

        return count

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
        self.__session.add(obj)

    # -------------------------------------------------------------------------

    def save(self):
        """Save changes to the current session.
        Returns nothing.
        """
        self.__session.commit()

    # -------------------------------------------------------------------------

    def reload(self):
        """Reload data from the database.
        Returns nothing.
        """
        Base.metadata.create_all(self.__engine)
        session_create = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_create)
        self.__session = Session

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
