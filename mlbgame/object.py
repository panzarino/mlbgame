#!/usr/bin/env python

"""Module that is used for holding basic objects"""

class Object(object):
    """Basic class"""
    
    def __init__(self, data):
        """Creates an object that matches the corresponding stats in `data`.
        
        `data` should be an dictionary of values.
        """
        # loop through data
        for x in data:
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    setattr(self, x, str(data[x]))
