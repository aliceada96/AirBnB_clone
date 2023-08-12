#!/usr/bin/python3
"""This module defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """A class to represent a user.

    Attributes:
        email (str): The user's email.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
