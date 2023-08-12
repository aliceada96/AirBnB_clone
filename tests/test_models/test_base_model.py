#!/usr/bin/python3
"""This module defines tests for the BaseModel class."""

import unittest
import uuid
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel functionality.

    Args:
        unittest (module): inherit functionality from unittest's TestCase class
    """

    instance1 = ""
    instance2 = ""
    instance3 = ""

    @classmethod
    def setUpClass(cls) -> None:
        """This method is called once before any tests are run.

        It can be used to set up any expensive resources
        that need to be shared across the test methods.
        """
        cls.instances = []
        # return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        """This method is called once after all tests are run.

        It can be used to clean up any resources that were created
        in the setUpClass method.
        """
        cls.instances.clear()
        # return super().tearDownClass()

    def setUp(self) -> None:
        """This method is called b4 each test to set up the initial state."""
        self.instance1 = BaseModel()
        self.instance2 = BaseModel()
        self.instance3 = BaseModel()
        # return super().setUp()

    def tearDown(self) -> None:
        """Call after each test method is run.

        It can be used to clean up any resources that were created
        in the setUp method.
        """
        del storage.all()["{}.{}".format("BaseModel", self.instance1.id)]
        del storage.all()["{}.{}".format("BaseModel", self.instance2.id)]
        del storage.all()["{}.{}".format("BaseModel", self.instance3.id)]
        self.instances.clear()

    # TESTS FOR __INIT__, REPR AND STR METHODS
    def test__init__(self):
        """Test that an instance is created successfully."""
        self.instance1 = BaseModel()
        self.assertIsInstance(self.instance1, BaseModel)
        self.assertIn("id", self.instance1.__dict__.keys())
        self.assertIn("created_at", self.instance1.__dict__.keys())
        self.assertIn("updated_at", self.instance1.__dict__.keys())
        self.assertIsInstance(self.instance1.id, str)
        self.assertIsInstance(self.instance1.created_at, datetime.datetime)
        self.assertIsInstance(self.instance1.updated_at, datetime.datetime)
        # self.assertEqual(len(self.instance1.id), UUID_LENGHT + 4)
        # self.instance1 attributes added successfully
        self.instance1.name = "My First Model"
        self.instance1.my_number = 89
        self.assertIn("name", self.instance1.__dict__.keys())
        self.assertIn("my_number", self.instance1.__dict__.keys())

    def test__str__(self):
        """Test the str() method returns a correct printed instance format."""
        self.instance1 = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(
            self.instance1.id, self.instance1.__dict__
        )
        self.assertEqual(str(self.instance1), expected_output)

    def test_id_uniqueness(self):
        """Test if each instance has a unique id.

        Returns:
          None
        """
        self.assertNotEqual(self.instance1.id, self.instance2.id)
        self.assertNotEqual(self.instance2.id, self.instance3.id)
        self.assertNotEqual(self.instance3.id, self.instance1.id)

    def test_save(self):
        """Test save method updates the updated_at.

        And that updated_at is at a later time than created at
        """
        self.instance1 = BaseModel()
        self.instance1.save()
        self.assertNotEqual(
            self.instance1.created_at, self.instance1.updated_at)
        self.assertGreater(
            self.instance1.updated_at, self.instance1.created_at)

    def test_to_dict(self):
        """Test if the dict representation contains all keys"""
        self.instance1 = BaseModel()
        # Checks that all the keys were created
        expectedKeys = ["id", "created_at", "updated_at"]
        actualDict = self.instance1.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertTrue((key in list(actualDict)))
        # Checks that the method returns a dictionary
        self.assertIsInstance(self.instance1.to_dict(), dict)
        # cheks for correct type(str) for each key
        actualDict = self.instance1.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertIsInstance(self.instance1.to_dict()[key], str)
        # Checks that the key:values match the instances
        instance_dict = self.instance1.to_dict()
        self.assertEqual(instance_dict["id"], self.instance1.id)
        self.assertEqual(
            instance_dict["created_at"], self.instance1.created_at.isoformat()
        )
        self.assertEqual(
            instance_dict["updated_at"], self.instance1.updated_at.isoformat()
        )
