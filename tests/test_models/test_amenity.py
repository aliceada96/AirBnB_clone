#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    def test_instance_creation(self):
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_amenity_attributes(self):
        instance = Amenity(name="WiFi")
        self.assertEqual(instance.name, "WiFi")
