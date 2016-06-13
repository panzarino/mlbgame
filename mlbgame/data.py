#!/usr/bin/env python

"""This module gets the XML data that other functions use.
It checks if the data is cached first, and if not, 
gets the data from mlb.com.
"""

import os
try:
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import urlopen, HTTPError

def get_scoreboard(year, month, day):
    """Return the game file for a certain day matching certain criteria."""
    # add zeros if less than 10
    monthstr = str(month).zfill(2)
    daystr = str(day).zfill(2)
    # file
    filename = "gameday-data/year_%i/month_%s/day_%s/scoreboard.xml.gz" % (year, monthstr, daystr)
    file = os.path.join(os.path.dirname(__file__), filename)
    # check if file exits
    if os.path.isfile(file):
        data = file
    else:
        # get data if file does not exist
        try:
            data = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/scoreboard.xml" % (year, monthstr, daystr))
        except HTTPError:
            data = os.path.join(os.path.dirname(__file__), "gameday-data/default.xml")
    return data

def get_box_score(game_id):
    """Return the box score file of a game with matching id."""
    # get relevant information from game id
    year, month, day, rest = game_id.split('_', 3)
    # file
    filename = "gameday-data/year_%s/month_%s/day_%s/gid_%s/boxscore.xml" % (year, month, day, game_id)
    file = os.path.join(os.path.dirname(__file__), filename)
    # check if file exits
    if os.path.isfile(file):
        data = file
    else:
        # get data if file does not exist
        try:
            data = urlopen("http://gd2.mlb.com/components/game/mlb/year_%s/month_%s/day_%s/gid_%s/boxscore.xml" % (year, month, day, game_id))
        except HTTPError:
            raise ValueError("Could not find a game with that id.")
    return data

def get_game_events(game_id):
    """Return the game events file of a game with matching id."""
    # get relevant information from game id
    year, month, day, rest = game_id.split('_', 3)
    # file
    filename = "gameday-data/year_%s/month_%s/day_%s/gid_%s/game_events.xml" % (year, month, day, game_id)
    file = os.path.join(os.path.dirname(__file__), filename)
    # check if file exits
    if os.path.isfile(file):
        data = file
    else:
        # get data if file does not exist
        try:
            data = urlopen("http://gd2.mlb.com/components/game/mlb/year_%s/month_%s/day_%s/gid_%s/game_events.xml" % (year, month, day, game_id))
        except HTTPError:
            raise ValueError("Could not find a game with that id.")
    return data
