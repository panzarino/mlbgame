#!/usr/bin/env python

"""Module that is used for holding basic objects"""


def setobjattr(obj, key, value):
    """Sets an object attribute with the correct data type."""
    try:
        setattr(obj, key, int(value))
    except ValueError:
        try:
            setattr(obj, key, float(value))
        except ValueError:
            # string if not number
            try:
                setattr(obj, key, str(value))
            except UnicodeEncodeError:
                setattr(obj, key, value)


class Object(object):
    """Basic class"""

    def __init__(self, data):
        """Creates an object that matches the corresponding values in `data`.

        `data` should be a dictionary of values.
        """
        # loop through data
        for x in data:
            setobjattr(self, x, data[x])
