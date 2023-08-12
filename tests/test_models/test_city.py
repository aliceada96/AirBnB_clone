#!/usr/bin/python3
"""This module defines unit tests for the City class."""

import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """Test class for the City class."""

    def test_instance_creation(self):
        """Test if an instance of City is created successfully."""
        instance = City()
        self.assertIsInstance(instance, City)

    def test_city_attributes(self):
        """Test City attributes."""
        instance = City(state_id="KEN", name="Nairobi")
        self.assertEqual(instance.state_id, "KEN")
        self.assertEqual(instance.name, "Nairobi")
