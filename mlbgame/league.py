#!/usr/bin/env python

"""Module that is used for getting information
about the (MLB) league and the teams in it.
"""

import mlbgame.data

import lxml.etree as etree

def get_league_object():
    """Returns the xml object corresponding to the league
    
    Only designed for internal use"""
    # get data
    data = mlbgame.data.get_properties()
    # return league object
    return etree.parse(data).getroot().find("leagues").find("league")