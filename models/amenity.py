#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class to represent an amenity

    Args:
        name (str): Amenity name
    """

    name = ""
