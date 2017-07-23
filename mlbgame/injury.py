#!/usr/bin/env python

"""
Module that is used for getting the MLB injuries.
"""
from __future__ import print_function

import sys
import dateutil.parser
import requests


class Injury(object):
    """Represents the MLB Disabled List

    Properties:
        injury_url
        injuries
        team_id
        injury_json
        last_update
    """
    injury_url = 'http://mlb.mlb.com/fantasylookup/json/named.wsfb_news_injury.bam'

    def __init__(self, team_id=None):
        if team_id:
            self.injury_url = Injury.injury_url
            self.injuries = []
            if isinstance(team_id, int):
                self.team_id = str(team_id)
            else:
                try:
                    raise TeamIDException('A `team_id` must be an integer.')
                except TeamIDException as e:
                    print(e)
                    raise
            self.parse_injury()
        else:
            try:
                raise TeamIDException('A `team_id` was not supplied.')
            except TeamIDException as e:
                print(e)
                raise

    @property
    def injury_json(self):
        """Return injury output as json"""
        try:
            return requests.get(self.injury_url).json()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(-1)

    @property
    def last_update(self):
        """Return a dateutil object from string [last update]
        originally in ISO 8601 format: YYYY-mm-ddTHH:MM:SS"""
        last_update = self.injury_json['wsfb_news_injury']['queryResults']['created']
        return dateutil.parser.parse(last_update)

    def parse_injury(self):
        """Parse the json injury"""
        injuries = self.injury_json['wsfb_news_injury']['queryResults']['row']
        injuries = [ injury for injury in injuries if injury['team_id'] == self.team_id ]
        for injury in injuries:
            mlbinjury = type('Player', (object,), injury)
            self.injuries.append(mlbinjury)


class injuryException(Exception):
    """injury Exceptions"""


class TeamIDException(injuryException):
    """A `team_id` was not supplied or the `team_id` was not an integer."""


#
# @meta_classes
#

#class Player(object):
#    """Represents an MLB injury
#
#    Properties:
#        display_ts
#        due_back"
#        injury_desc
#        injury_status
#        injury_update
#        insert_ts
#        league_id
#        name_first
#        name_last
#        player_id
#        position
#        team_id
#        team_name
