#!/usr/bin/python3
"""This module defines unit tests for the Amenity class."""

import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Test class for the Amenity class."""

    def test_instance_creation(self):
        """Test if an instance of Amenity is created successfully."""
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_amenity_attributes(self):
        """Test Amenity attributes."""
        instance = Amenity(name="WiFi")
        self.assertEqual(instance.name, "WiFi")
