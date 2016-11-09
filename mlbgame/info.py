#!/usr/bin/env python

"""Module that is used for getting information
about the (MLB) league and the teams in it.
"""

import mlbgame.data
import mlbgame.object

import lxml.etree as etree

def get_league_object():
    """Returns the xml object corresponding to the league
    
    Only designed for internal use"""
    # get data
    data = mlbgame.data.get_properties()
    # return league object
    return etree.parse(data).getroot().find("leagues").find("league")

def league_info():
    """Returns a dictionary of league information"""
    league = get_league_object()
    output = {}
    for x in league.attrib:
        output[x] = league.attrib[x]
    return output

def team_info():
    """Returns a list of team information dictionaries"""
    teams = get_league_object().find("teams").findall("team")
    output = []
    for team in teams:
        info = {}
        for x in team.attrib:
            info[x] = team.attrib[x]
        output.append(info)
    return output

class Info(mlbgame.object.Object):
    """Holds information about the league or teams"""

    def nice_output(self):
        """Return a string for printing"""
        return '%s (%s)' % (self.club_full_name, self.club)

    def __str__(self):
        return self.nice_output()

