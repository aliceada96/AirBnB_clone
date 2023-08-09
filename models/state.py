#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """Class to represent a state

    Args:
        name (str): Name of state
    """

    name = ""
