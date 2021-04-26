"""
This file (test_models.py) contains the unit tests for the model XYData3.
"""
from app import XYData3


def test_create_new():
    """
    GIVEN a XYData3 database model
    WHEN a new XYData3 is created
    THEN check the description, owner, x, and y fields are defined correctly
    """
    xydata = XYData3('Descr', 'MJ', '1,2,3', '4,5,6')
    assert xydata.description == 'Descr'
    assert xydata.owner == 'MJ'
    assert xydata.x == '1,2,3'
    assert xydata.y == '4,5,6'
