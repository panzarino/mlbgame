#!/usr/bin/env python

"""Module that is used for getting the events 
that occured throughout games.
"""

import lxml.etree as etree
import mlbgame.data

def game_events(game_id):
    """Return dictionary of events for a game with matching id."""
    # get data from data module
    data = mlbgame.data.get_game_events(game_id)
    # parse XML
    parsed = etree.parse(data)
    root = parsed.getroot()
    # empty output file
    output = {}
    # loop through innings
    innings = root.findall('inning')
    for x in innings:
        # loop through the top half
        top = x.findall('top')[0]
        for y in top.findall('atbat'):
            pass
        # loop through the bottom half
        bot = x.findall('bottom')[0]
        for y in bot.findall('atbat'):
            pass
        

class Event(object):
    def __init__(self, data):
        """Creates an event object that matches the corresponding info in `data`.
        
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
