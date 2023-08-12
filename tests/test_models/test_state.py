#!/usr/bin/python3
"""This module defines unit tests for the State class."""

import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """Test class for the State class"""

    def test_instance_creation(self):
        """Test if an instance of State is created successfully."""
        instance = State()
        self.assertIsInstance(instance, State)

    def test_state_attributes(self):
        """Test State attributes."""
        instance = State(name="Kenya")
        self.assertEqual(instance.name, "Kenya")
