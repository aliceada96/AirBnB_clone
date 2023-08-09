#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User class

    Args:
        email (str): User's email
        password (str) - User's password
        first_name (str): user's first name
        last_name (str): User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
