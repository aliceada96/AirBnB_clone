#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Args:
        place_id (str): the Place.id
        user_id (str): the User.id
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
