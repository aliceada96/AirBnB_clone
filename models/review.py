#!/usr/bin/python3
"""This module defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class to represent a review.

    Attributes:
        place_id (str): The ID of the associated place.
        user_id (str): The ID of the associated user.
        text (str): The review text.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance."""
        super().__init__(*args, **kwargs)

    place_id = ""
    user_id = ""
    text = ""
