#!/usr/bin/env python

"""
Module that is used for getting the MLB rosters.
"""

from __future__ import print_function

import sys
import dateutil.parser
import requests


class Roster(object):
    """Represents an MLB Team

    Properties:
        roster_url
        roster
        roster_json
        last_update
    """
    roster_url = 'http://mlb.mlb.com/lookup/json/named.roster_40.bam?team_id=%s'

    def __init__(self, team_id=None):
        if team_id:
            self.roster_url = Roster.roster_url % team_id
            self.roster = []
            self.parse_roster()
        else:
            try:
                raise NoTeamID('A `team_id` was not supplied.')
            except NoTeamID as e:
                print(e)
                raise

    @property
    def roster_json(self):
        """Return roster output as json"""
        try:
            return requests.get(self.roster_url).json()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(-1)

    @property
    def last_update(self):
        """Return a dateutil object from string [last update]
        originally in ISO 8601 format: YYYY-mm-ddTHH:MM:SS"""
        last_update = self.roster_json['roster_40']['queryResults']['created']
        return dateutil.parser.parse(last_update)

    def parse_roster(self):
        """Parse the json roster"""
        players = self.roster_json['roster_40']['queryResults']['row']
        for player in players:
            mlbplayer = type('Player', (object,), player)
            self.roster.append(mlbplayer)


class RosterException(Exception):
    """Roster Exceptions"""


class NoTeamID(RosterException):
    """A `team_id` was not supplied"""


#
# @meta_classes
#

#class Player(object):
#    """Represents an MLB Player
#
#    Properties:
#        position_txt
#        weight
#        name_display_first_last
#        college
#        height_inches
#        starter_sw
#        jersey_number
#        end_date
#        name_first
#        bats
#        team_code
#        height_feet
#        pro_debut_date
#        status_code
#        primary_position
#        birth_date
#        team_abbrev
#        throws
#        team_name
#        name_display_last_first
#        name_use
#        player_id
#        name_last
#        team_id
#        start_date
#        name_full
#    """
