#!/usr/bin/python3
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    def test_instance_creation(self):
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_review_attributes(self):
        instance = Review(
            place_id="Penthouse123",
            user_id="gabby_com",
            text="Great place to stay!"
        )
        self.assertEqual(instance.place_id, "Penthouse123")
        self.assertEqual(instance.user_id, "gabby_com")
        self.assertEqual(instance.text, "Great place to stay!")
