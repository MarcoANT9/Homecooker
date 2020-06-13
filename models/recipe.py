#!/usr/bin/python3
"""This class defines a recipe."""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship


class Recipe(BaseModel, Base):
    """This class defines a recipe"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    if models.stora_type == "db":
        """---MySQL-definitions----"""
        __tablename__ = 'Recipes'
        user_id = Column(String(60), ForeignKey('Users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        text = Column(String(2048), nullable=False)
        review = Column(Integer, nullable=False)
        ingredients = Column(String(1048), nullable=False)

        """---MySQL-Relationships----"""
        reviews = relationship("Review",
                               backref="recipe",
                               cascade="all, delete, delete-orphan")

    else:
        user_id = ""
        name = ""
        text = ""
        review = ""
        ingredients = ""

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

    """-----------"""
    """- Class ---"""
    """-----------"""

    """-----------"""
    """- Static --"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
    if models.stora_type != "db":
        @property
        def reviews(self):
            """Getter for all reviews linked to this recipe."""
            from models.review import Review
            linked_review = []
            all_review = models.storage.all(Review)
            for element in all_review.values():
                if element.recipe_id == self.id:
                    linked_review.append(element)
            return linked_review
