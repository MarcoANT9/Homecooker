#!/usr/bin/python3
"""This class defines a recipe."""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Foregnkey, Table, Integer


class Recipe(BaseModel, Base):
    """This class defines a recipe"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    """---MySQL-definitions----"""
    __tablename__ = 'recipes'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    text = Column(String(2048), nullable=False)
    review = Column(Integer, nulable=False)
    ingredients = Column(String(1048), nullable=False)

    """---MySQL-Relationships----"""
    reviews = relationship('Review',
                           backref="recipes",
                           cascade="all, delete, delete-orphan")

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
