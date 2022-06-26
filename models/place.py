#!/usr/bin/python3
"""
Defines a class Place
"""

from models.base_model import BaseModel


class Place:
    """
    Class Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = 0.0
    longitude = 0.0
    # list of Amenity id
    amenity_ids = []
