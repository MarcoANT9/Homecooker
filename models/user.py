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
    recipes = relationship('Recipe'
                           backref="users",
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
