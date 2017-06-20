#!/usr/bin/env python

"""This module gets the XML data that other functions use.
It checks if the data is cached first, and if not,
gets the data from mlb.com.
"""

import os
import sys

try:
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import urlopen, HTTPError


# Templates For Local Paths and URLS
BASE_URL = "http://gd2.mlb.com/components/game/mlb/year_{0}/month_{1}/day_{2}/"
GAME_URL = BASE_URL + "/gid_{3}/{4}"
BASE_PATH = "gameday-data/year_{0}/month_{1}/day_{2}/"
GAME_PATH = BASE_PATH + "gid_{3}{4}/"

PROPERTY_URL = "http://mlb.mlb.com/properties/mlb_properties.xml"
# Local Directory
PWD = os.path.join(os.path.dirname(__file__))


def get_scoreboard(year, month, day):
    """Return the game file for a certain day matching certain criteria."""
    # add zeros if less than 10
    monthstr = str(month).zfill(2)
    daystr = str(day).zfill(2)
    # file
    local_filename = BASE_PATH.format(year, monthstr, daystr) + "scoreboard.xml.gz"
    local_file = os.path.join(PWD, local_filename)
    # check if file exits
    if os.path.isfile(local_file):
        if sys.platform == 'win32':
            file_unzipped = local_file[:-3]
            if not os.path.exists(file_unzipped):
                import gzip
                with(gzip.open(local_file, 'rb')) as f_gz:
                    with(open(file_unzipped, 'wb')) as f:
                        f.write(f_gz.read())
        return local_file
    # get data if file does not exist
    try:
        data = urlopen(BASE_URL.format(year, monthstr, daystr) + "scoreboard.xml")
    except HTTPError:
        data = os.path.join(PWD, "gameday-data/default.xml")
    return data


def get_box_score(game_id):
    """Return the box score file of a game with matching id."""
    # file
    year, month, day = get_date_from_game_id(game_id)
    local_filename = GAME_PATH.format(year, month, day , game_id, "boxscore.xml")
    local_file = os.path.join(PWD, local_filename)
    # check if file exits
    if os.path.isfile(local_file):
        return local_file
    # get data if file does not exist
    try:
        return urlopen(GAME_URL.format(year, month, day , game_id, "boxscore.xml"))
    except HTTPError:
        raise ValueError("Could not find a game with that id.")


def get_game_events(game_id):
    """Return the game events file of a game with matching id."""
    # file
    year, month, day = get_date_from_game_id(game_id)
    local_filename = GAME_PATH.format(year, month, day, game_id, game_id, "game_events.xml")
    local_file = os.path.join(PWD, local_filename)
    # check if file exits
    if os.path.isfile(local_file):
        return local_file
    # get data if file does not exist
    try:
        return urlopen(GAME_URL.format(year, month, day, game_id, "game_events.xml"))
    except HTTPError:
        raise ValueError("Could not find a game with that id.")


def get_overview(game_id):
    """Return the linescore file of a game with matching id."""
    # file
    year, month, day = get_date_from_game_id(game_id)
    local_filename = GAME_PATH.format(year, month, day, game_id, "linescore.xml")
    local_file = os.path.join(PWD, local_filename)
    # check if file exits
    if os.path.isfile(local_file):
        return local_file
        # get data if file does not exist
    try:
        return urlopen(GAME_URL.format(year, month, day, game_id, "linescore.xml"))
    except HTTPError:
        raise ValueError("Could not find a game with that id.")


def get_properties():
    """Return the current mlb properties file"""
    try:
        return urlopen(PROPERTY_URL)
    # in case mlb.com depricates this functionality
    except HTTPError:
        raise ValueError("Could not find the properties file. "
                         "mlb.com does not provide the file that mlbgame needs to perform this operation.")


def get_date_from_game_id(game_id):
    year, month, day, _discard = game_id.split('_', 3)
    return year, month, day
