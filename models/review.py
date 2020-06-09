#!/usr/bin/python3
"""This class defines a review"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Foregnkey, Table, Integer


class Review(BaseModel, Base):
    """This class defines a review"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    if models.stora_type == "db":
        """---MySQL-definitions----"""
        __tablename__ = 'Reviews'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)
        text = Column(String(1024), nullable=False)
        rating = Column(Integer, nullable=False)

        """---MySQL-Relationships----"""
    else:
        user_id = ""
        recipe_id = ""
        text = ""
        rating = 0


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
