#!/usr/bin/python3

import unittest
from models.state import State


class Test_State(unittest.TestCase):
    def test_instance_creation(self):
        instance = State()
        self.assertIsInstance(instance, State)

    def test_state_attributes(self):
        instance = State(name="Kenya")
        self.assertEqual(instance.name, "Kenya")
