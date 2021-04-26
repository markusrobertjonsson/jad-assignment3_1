"""
This file (test_models.py) contains the unit tests for the model DataOwner.
"""
import unittest

from app import DataOwner


class TestBasic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_new(self):
        """
        GIVEN a DataOwner database model
        WHEN a new DataOwner is created
        THEN check the name, age, and email fields are defined correctly
        """
        owner = DataOwner(name='My Name', age=40, email='my_name@mail.com')
        assert owner.name == 'My Name'
        assert owner.age == 40
        assert owner.email == 'my_name@mail.com'
