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
        topinfo = []
        # loop through the top half
        top = x.findall('top')[0]
        for y in top.findall('atbat'):
            atbat = {}
            # loop through and save info
            for i in y.attrib:
                atbat[i] = y.attrib[i]
            atbat['pitches'] = []
            for i in y.findall('pitch'):
                pitch = {}
                # loop through pitch info
                for n in i.attrib:
                    pitch[n] = i.attrib[n]
                atbat['pitches'].append(pitch)
            topinfo.append(atbat)
        # loop through the bottom half
        bot = x.findall('bottom')[0]
        for y in bot.findall('atbat'):
            # top info
            botinfo = []
            # loop through the top half
            bot = x.findall('top')[0]
            for y in bot.findall('atbat'):
                atbat = {}
                # loop through and save info
                for i in y.attrib:
                    atbat[i] = y.attrib[i]
                atbat['pitches'] = []
                for i in y.findall('pitch'):
                    pitch = {}
                    # loop through pitch info
                    for n in i.attrib:
                        pitch[n] = i.attrib[n]
                    atbat['pitches'].append(pitch)
                botinfo.append(atbat)
        output[x.attrib['num']] = {'top': topinfo, 'bottom': botinfo}
    return output

class AtBat(object):
    """Class that holds information about at bats in games.
    
    Properties: 
    
    - num = Number of at bat in game
    - b = balls (at end of at bat or currently if live)
    - s = strikes (at end of at bat or currently if live)
    - o = outs (at end of at bat)
    - batter = batter id number
    - pitcher = pitcher id number
    - des = description of at bat
    - event_num = number that corresponds to type of event
    - event = name of event
    - home_team_runs = home team runs (at end of at bat)
    - away_team_runs = away team runs (at end of at bat)
    - pitches = list of pitches during at bat
    - b1
    - b2
    - b3
    """
    
    def __init__(self, data):
        """Creates an event object that matches the corresponding info in `data`.
        
        `data` should be an dictionary of values.
        """
        # loop through data
        for x in data:
            # remove spanish info (causes text encoding errors)
            if '_es' in x:
                continue
            # create pitches list if attribute name is pitches
            if x == 'pitches':
                self.pitches = []
                for y in data[x]:
                    self.pitches.append(Pitch(y))
                continue
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    setattr(self, x, str(data[x]))
    
    def nice_output(self):
        """Prints basic event info in a nice way."""
        return self.des
    
    def __str__(self):
        return self.nice_output()

class Pitch(object):
    """Class that holds information about individual pitches.
    
    Properties of pitches are wildly inconsistent, 
    sometimes they have a value, sometimes they don't.
    Properties:
    
    - sv_id
    - des = description of pitch outcome
    - type = ball (B), strike (S), or in play (X)
    - start_speed = pitch speed
    - pitch_type = type of pitch (fastball, curve, etc.)
    """
    
    def __init__(self, data):
        """Creates a pitch object that matches the corresponding info in `data`.
        
        `data` should be an dictionary of values.
        """
        # loop through data
        for x in data:
            # remove spanish info (causes text encoding errors)
            if '_es' in x:
                continue
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    setattr(self, x, str(data[x]))
    
    def nice_output(self):
        """Prints basic event info in a nice way."""
        return "Pitch: %s at %s: %s" % (self.pitch_type, self.start_speed, self.des)
    
    def __str__(self):
        return self.nice_output()
