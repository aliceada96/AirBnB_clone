#!/usr/bin/python3
import unittest
from models.user import User


class Test_User(unittest.TestCase):

    instance = ""

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
        self.instance = User(
            email="user@example.com",
            password="secretpassword01",
            first_name="Ada",
            last_name="Alice",
        )
        # return super().setUp()

    def tearDown(self) -> None:
        """This method is called after each test method is run.
        It can be used to clean up any resources that were created
        in the setUp method."""
        del self.instance
        self.instances.clear()
        # return super().tearDown()

    def test_instance_creation(self):
        self.assertIsInstance(self.instance, User)

    def test_user_attributes(self):

        self.assertEqual(self.instance.email, "user@example.com")
        self.assertEqual(self.instance.password, "secretpassword01")
        self.assertEqual(self.instance.first_name, "Ada")
        self.assertEqual(self.instance.last_name, "Alice")
