#!/usr/bin/python3
"""This module defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """A class to represent a city.

    Attributes:
        state_id (str): The ID of the associated state.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new City instance."""
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""
