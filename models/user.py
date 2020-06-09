#!/usr/bin/python3
"""This class defines a user"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Table, LargeBinary
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    if models.stora_type == "db":
        """---MySLQ-definitions----"""
        __tablename__ = 'Users'
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        website = Column(String(256), nullable=True)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        user_type = Column(Integer, nullable=False)
        profile_image = Column(LargeBinary, nullable=True)
        nickname = Column(String(128), nullable=True)

        """---MySQL-relationships----"""
        reviews = relationship('Review',
                               backref="users",
                               cascade="all, delete, delete-orphan")
        recipes = relationship('Recipe',
                               backref="users",
                               cascade="all, delete, delete-orphan")
    else:
        first_name = ""
        last_name = ""
        website = ""
        email = ""
        password = ""
        user_type = 0
        profile_image = 0
        nickname = ""

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """----------"""
    """- Public -"""
    """----------"""

    """-----------"""
    """- Private -"""
    """-----------"""
    def __setattr__(self, name, value):
        """Modify the password to md5 encryption algorithm"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    """-----------"""
    """- Class ---"""
    """-----------"""

    """-----------"""
    """- Static --"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
    if models.stora_type != 'db':
        @property
        def recipes(self):
            """Getter attribute that links this object to recipes instances."""
            from models.recipe import Recipe
            linked_recipe = []
            all_recipe = model.storage.all(Recipe)
            for element in all_recipe.values():
                if element.user_id == self.id:
                    linked_recipe.append(element)
            return linked_recipe

        @property
        def reviews(self):
            """Getter attribute that links this object to review instances."""
            from models.review import Review
            linked_review = []
            all_review = model.storage.all(Review)
            for element in all_review.values():
                if element.user_id == self.id:
                    linked_review.append(element)
            return linked_list
