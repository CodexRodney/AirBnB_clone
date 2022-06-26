#!/usr/bin/python3
"""
Defines a class user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
