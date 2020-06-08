#!/usr/bin/python3
"""This class defines a review"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Foregnkey, Table, Integer


class Review(BaseModel, Base):
    """This class defines a review"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    """---MySQL-definitions----"""
    __tablename__ = 'reviews'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)

    """---MySQL-Relationships----"""

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
