#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City class

    Args:
        state_id (str): state id
        name (str): name of city
    """

    state_id = ""
    name = ""
