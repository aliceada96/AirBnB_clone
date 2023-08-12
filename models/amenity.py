#!/usr/bin/python3
"""This module defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class to represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity instance."""
        super().__init__(*args, **kwargs)

    name = ""
