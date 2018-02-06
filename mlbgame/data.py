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


# Templates For URLS
BASE_URL = ('http://gd2.mlb.com/components/game/mlb/'
            'year_{0}/month_{1:02d}/day_{2:02d}/')
GAME_URL = BASE_URL + 'gid_{3}/{4}'
PROPERTY_URL = 'http://mlb.mlb.com/properties/mlb_properties.xml'
ROSTER_URL = 'http://mlb.mlb.com/lookup/json/named.roster_40.bam?team_id={0}'
INJURY_URL = 'http://mlb.mlb.com/fantasylookup/json/named.wsfb_news_injury.bam'
STANDINGS_URL = ('http://mlb.mlb.com/lookup/json/named.standings_schedule_date.bam?season={0}&'
                'schedule_game_date.game_date=%27{1}%27&sit_code=%27h0%27&league_id=103&'
                'league_id=104&all_star_sw=%27N%27&version=2')
STANDINGS_HISTORICAL_URL = ('http://mlb.mlb.com/lookup/json/named.historical_standings_schedule_date.bam?season={0}&'
                           'game_date=%27{1}%27&sit_code=%27h0%27&league_id=103&'
                           'league_id=104&all_star_sw=%27N%27&version=48')
# Local Directory
PWD = os.path.join(os.path.dirname(__file__))


def get_scoreboard(year, month, day):
    """Return the game file for a certain day matching certain criteria."""
    try:
        data = urlopen(BASE_URL.format(year, month, day
                                       ) + 'scoreboard.xml')
    except HTTPError:
        data = os.path.join(PWD, 'default.xml')
    return data


def get_box_score(game_id):
    """Return the box score file of a game with matching id."""
    year, month, day = get_date_from_game_id(game_id)
    try:
        return urlopen(GAME_URL.format(year, month, day,
                                       game_id,
                                       'boxscore.xml'))
    except HTTPError:
        raise ValueError('Could not find a game with that id.')

def get_raw_box_score(game_id):
    """Return the raw box score file of a game with matching id."""
    year, month, day = get_date_from_game_id(game_id)
    try:
        return urlopen(GAME_URL.format(year, month, day,
                                       game_id,
                                       'rawboxscore.xml'))
    except HTTPError:
        raise ValueError('Could not find a game with that id.')


def get_game_events(game_id):
    """Return the game events file of a game with matching id."""
    year, month, day = get_date_from_game_id(game_id)
    try:
        return urlopen(GAME_URL.format(year, month, day,
                                       game_id,
                                       'game_events.xml'))
    except HTTPError:
        raise ValueError('Could not find a game with that id.')


def get_overview(game_id):
    """Return the linescore file of a game with matching id."""
    year, month, day = get_date_from_game_id(game_id)
    try:
        return urlopen(GAME_URL.format(year, month, day,
                                       game_id,
                                       'linescore.xml'))
    except HTTPError:
        raise ValueError('Could not find a game with that id.')


def get_players(game_id):
    """Return the players file of a game with matching id."""
    year, month, day = get_date_from_game_id(game_id)
    try:
        return urlopen(GAME_URL.format(year, month, day,
                                       game_id,
                                       "players.xml"))
    except HTTPError:
        raise ValueError('Could not find a game with that id.')


def get_properties():
    """Return the current mlb properties file"""
    try:
        return urlopen(PROPERTY_URL)
    # in case mlb.com depricates this functionality
    except HTTPError:
        raise ValueError('Could not find the properties file. '
                         'mlb.com does not provide the file that '
                         'mlbgame needs to perform this operation.')


def get_roster(team_id):
    """Return the roster file of team with matching id."""
    try:
        return urlopen(ROSTER_URL.format(team_id))
    except HTTPError:
        raise ValueError('Could not find a roster for a team with that id.')


def get_standings(date):
    """Return the standings file for current standings (given current date)."""
    try:
        return urlopen(STANDINGS_URL.format(date.year, date.strftime('%Y/%m/%d')))
    except HTTPError:
        ValueError('Could not find the standings file. '
                   'mlb.com does not provide the file that '
                   'mlbgame needs to perform this operation.')


def get_historical_standings(date):
    """Return the historical standings file for specified date."""
    try:
        return urlopen(STANDINGS_HISTORICAL_URL.format(date.year, date.strftime('%Y/%m/%d')))
    except HTTPError:
        ValueError('Could not find standings for that date.')


def get_injuries():
    """Return the injuries file for specified date."""
    try:
        return urlopen(INJURY_URL)
    except HTTPError:
        ValueError('Could not find the injuries file. '
                   'mlb.com does not provide the file that '
                   'mlbgame needs to perform this operation.')


def get_date_from_game_id(game_id):
    year, month, day, _discard = game_id.split('_', 3)
    return int(year), int(month), int(day)
