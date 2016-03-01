#!/usr/bin/env python

"""Module that controls getting stats and creating objects to hold that information."""

import lxml.etree as etree
import mlbgame.data

def player_stats(game_id):
    """Return dictionary of individual stats of a game with matching id."""
    # get data from data module
    data = mlbgame.data.get_box_score(game_id)
    # parse XML
    parsed = etree.parse(data)
    root = parsed.getroot()
    # get pitching and batting info
    pitching = root.findall('pitching')
    batting = root.findall('batting')
    # empty lists for output
    home_pitching = []
    away_pitching = []
    home_batting = []
    away_batting = []
    # loop through pitching info
    for y in pitching:
        # checks if home team
        home=False
        if y.attrib['team_flag'] == "home":
            home = True
        # loops through pitchers
        for x in y.findall('pitcher'):
            stats = {}
            # loop through and save stats
            for i in x.attrib:
                stats[i]=x.attrib[i]
            # apply to correct list
            if home:
                home_pitching.append(stats)
            elif not home:
                away_pitching.append(stats)
    # loop through batting info
    for y in batting:
        # checks if home team
        home=False
        if y.attrib['team_flag'] == "home":
            home = True
        # loops through batters
        for x in y.findall('batter'):
            stats = {}
            # loop through and save stats
            for i in x.attrib:
                stats[i]=x.attrib[i]
            # apply to correct list
            if home:
                home_batting.append(stats)
            elif not home:
                away_batting.append(stats)
    # put lists in dictionary for output
    output = {'home_pitching':home_pitching, 'away_pitching':away_pitching, 'home_batting':home_batting, 'away_batting':away_batting}
    return output

def team_stats(game_id):
    """Return team stats of a game with matching id."""
    # get data from data module
    data = mlbgame.data.get_box_score(game_id)
    # parse XML
    parsed = etree.parse(data)
    root = parsed.getroot()
    # get pitching and batting ingo
    pitching = root.findall('pitching')
    batting = root.findall('batting')
    # dictionary for output
    output = {}
    # loop through pitching info
    for x in pitching:
        stats = {}
        # loop through stats and save
        for y in x.attrib:
            stats[y] = x.attrib[y]
        # apply to correct team
        if x.attrib['team_flag']=='home':
            output['home_pitching']=stats
        elif x.attrib['team_flag']=='away':
            output['away_pitching']=stats
    # loop through pitching info
    for x in batting:
        stats = {}
        # loop through stats and save
        for y in x.attrib:
            stats[y] = x.attrib[y]
        # apply to correct team
        if x.attrib['team_flag']=='home':
            output['home_batting']=stats
        elif x.attrib['team_flag']=='away':
            output['away_batting']=stats
    return output

class Stats(object):
    """Basic stats class for any type of stats."""
    
    def __init__(self, data):
        """Creates a stats object that matches the corresponding stats in `data`.
        
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

class PitcherStats(Stats):
    """Holds stats information for a pitcher.
    
    Check out `statmap.py` for a full list of object properties.
    """

    def nice_output(self):
        """Prints basic pitcher stats in a nice way."""
        return "%s - %i Earned Runs, %i Strikouts, %i Hits" % (self.name_display_first_last, self.er, self.so, self.h)
    
    def __str__(self):
        return self.nice_output()

class BatterStats(Stats):
    """Holds stats information for a batter.
    
    Check out `statmap.py` for a full list of object properties.
    """
    
    def nice_output(self):
        """Prints basic batter stats in a nice way."""
        if self.rbi > 0:
            if self.hr > 0:
                # display home runs if he has any
                return "%s - %i for %i with %i RBI and %i Home Runs" % (self.name_display_first_last, self.h, self.ab, self.rbi, self.hr)
            # display RBI if he has any but no HR
            return "%s - %i for %i with %i RBI" % (self.name_display_first_last, self.h, self.ab, self.rbi)
        # display basic game stats
        return "%s - %i for %i" % (self.name_display_first_last, self.h, self.ab)
    
    def __str__(self):
        return self.nice_output()

class TeamStats(Stats):
    """Holds total pitching or batting stats for a team"""
    # basically a copy of the Stats class with a different name for clarification
    pass
