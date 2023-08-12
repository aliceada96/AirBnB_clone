#!/usr/bin/python3
"""This module defines the State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """A class to represent a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance."""
        super().__init__(*args, **kwargs)

    name = ""
