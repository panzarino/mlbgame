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
        # top info
        topinfo = {}
        # loop through the top half
        top = x.findall('top')[0]
        for y in top.findall('atbat'):
            atbat = {}
            # loop through and save info
            for i in y.attrib:
                atbat[i] = y.attrib[i]
            atbat['pitches'] = {}
            for i in y.findall('pitch'):
                for n in i.attrib:
                    atbat['pitches'][n] = i.attrib[n]
            topinfo[y.attrib['num']] = atbat
        # loop through the bottom half
        bot = x.findall('bottom')[0]
        for y in bot.findall('atbat'):
            # top info
            botinfo = {}
            # loop through the top half
            bot = x.findall('top')[0]
            for y in bot.findall('atbat'):
                atbat = {}
                # loop through and save info
                for i in y.attrib:
                    atbat[i] = y.attrib[i]
                atbat['pitches'] = {}
                for i in y.findall('pitch'):
                    for n in i.attrib:
                        atbat['pitches'][n] = i.attrib[n]
                botinfo[y.attrib['num']] = atbat
        output[x.attrib['num']] = {'top': topinfo, 'bot': botinfo}
    return output

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
