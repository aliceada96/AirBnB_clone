#!/usr/bin/python3
"""Unit tests for place module."""
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    def test_instance_creation(self):
        instance = Place()
        self.assertIsInstance(instance, Place)

    def test_place_attributes(self):
        instance = Place(
            city_id="NBO",
            user_id="gabby_com",
            name="Penthouse Apartment",
            description="Beautiful apartment in the city",
            number_rooms=4,
            number_bathrooms=4,
            max_guest=6,
            price_by_night=350,
            latitude=17.7649,
            longitude=-172.9194,
            amenity_ids=["wifi", "Swimming Pool", "parking"],
        )
        self.assertEqual(instance.city_id, "NBO")
        self.assertEqual(instance.user_id, "gabby_com")
        self.assertEqual(instance.name, "Penthouse Apartment")
        self.assertEqual(instance.description,
                         "Beautiful apartment in the city")
        self.assertEqual(instance.number_rooms, 4)
        self.assertEqual(instance.number_bathrooms, 4)
        self.assertEqual(instance.max_guest, 6)
        self.assertEqual(instance.price_by_night, 350)
        self.assertEqual(instance.latitude, 17.7649)
        self.assertEqual(instance.longitude, -172.9194)
        self.assertEqual(instance.amenity_ids,
                         ["wifi", "Swimming Pool", "parking"])
