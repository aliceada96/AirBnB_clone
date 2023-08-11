#!/usr/bin/python3
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    def test_instance_creation(self):
        instance = City()
        self.assertIsInstance(instance, City)

    def test_city_attributes(self):
        instance = City(state_id="KEN", name="Nairobi")
        self.assertEqual(instance.state_id, "KEN")
        self.assertEqual(instance.name, "Nairobi")
