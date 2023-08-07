#!/usr/bin/python3
"""tests

that the id is a uuid id

the .__str__() ouput a string of the specified format

that the created_at and updated_at are iso formats
"""

import unittest
import uuid
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel functionality
    Args:
        unittest (module): inherit functionality from unittest's TestCase class
    """

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
        """This method is called b4 each test case to set up
        the initial state."""
        pass
        # return super().setUp()

    def tearDown(self) -> None:
        """This method is called after each test method is run.
        It can be used to clean up any resources that were created
        in the setUp method."""
        self.instances.clear()
        # return super().tearDown()

    # TESTS FOR __INIT__, REPR AND STR METHODS
    def test__init__(self):
        """Test that an instance is created successfully"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIn("id", instance.__dict__.keys())
        self.assertIn("created_at", instance.__dict__.keys())
        self.assertIn("updated_at", instance.__dict__.keys())
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        # self.assertEqual(len(instance.id), UUID_LENGHT + 4)
        # instance attributes added successfully
        instance.name = "My First Model"
        instance.my_number = 89
        self.assertIn("name", instance.__dict__.keys())
        self.assertIn("my_number", instance.__dict__.keys())

    def test__repr__(self) -> str:
        pass
        # return super().__repr__()

    def test__str__(self):
        """Test that the __str__method returns the correct print format
        of an instance
        """
        instance = BaseModel()
        # self.assertAlmostEquals(instance.__str__(),
        #   "[BaseModel] (d7c81d7a-60fe-4851-a813-e2a185ea7723)
        #   {'id': 'd7c81d7a-60fe-4851-a813-e2a185ea7723',
        #    'created_at': datetime.datetime(2023, 8, 6, 21, 8, 7, 403778),
        #    'updated_at': datetime.datetime(2023, 8, 6, 21, 8, 46, 146227)}")

    def test_id_uniqueness(self):
        """
        Tests if each instance has a unique id.
        Returns:
        - None
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance2.id, instance3.id)
        self.assertNotEqual(instance3.id, instance1.id)

    def test_save(self):
        """Test that save method updates the updated_at
        and that updated_at is at a later time than created at
        """
        instance = BaseModel()
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)
        self.assertGreater(instance.updated_at, instance.created_at)

    def test_to_dict(self):
        """Tests to see if the dict representation contains all keys"""
        instance = BaseModel()
        expectedKeys = ["id", "created_at", "updated_at"]
        actualDict = instance.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertTrue((key in list(actualDict)))
        self.assertIsInstance(instance.to_dict(), dict)
        actualDict = instance.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertIsInstance(instance.to_dict()[key], str)
