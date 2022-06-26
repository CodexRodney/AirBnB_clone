#!/usr/bin/python3
"""
Defines a class City
"""

from models.base_model import BaseModel


class City(BaseModel):
    # it will be the State id
    state_id = ""
    name = ""
