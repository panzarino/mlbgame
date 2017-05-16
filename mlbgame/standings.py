#!/usr/bin/env python

"""
Module that is used for getting the MLB standings.
"""
from datetime import datetime
import sys
import dateutil.parser
import requests

class Standings(object):
    """Holds information about the league standings

    Properties:
        standings_url
        mlb_standings
        standings_json
        last_update
    """
    DIVISIONS = {
        'AL': {
            '201': 'AL East',
            '202': 'AL Central',
            '200': 'AL West',
        },
        'NL': {
            '204': 'NL East',
            '205': 'NL Central',
            '203': 'NL West',
        }
    }

    def __init__(self, date=datetime.now()):
        now = datetime.now()
        if date.year == now.year and date.month == now.month and date.day == now.day:
            self.standings_url = 'http://mlb.mlb.com/lookup/json/named.standings_schedule_date.bam?season=%s&' \
            'schedule_game_date.game_date=%%27%s%%27&sit_code=%%27h0%%27&league_id=103&' \
            'league_id=104&all_star_sw=%%27N%%27&version=2' % (date.year, date.strftime('%Y/%m/%d'))
            self.standings_schedule_date = 'standings_schedule_date'
        else:
            self.standings_url = 'http://mlb.mlb.com/lookup/json/named.historical_standings_schedule_date.bam?season=%s&' \
            'game_date=%%27%s%%27&sit_code=%%27h0%%27&league_id=103&' \
            'league_id=104&all_star_sw=%%27N%%27&version=48' % (date.year, date.strftime('%Y/%m/%d'))
            self.standings_schedule_date = 'historical_standings_schedule_date'
        self.mlb_standings = []
        self.parse_standings()

    @property
    def standings_json(self):
        """Return standings output as json"""
        try:
            return requests.get(self.standings_url).json()
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(-1)

    @property
    def divisions(self):
        """Return an array of Divison objects"""
        return self.mlb_standings

    @property
    def last_update(self):
        """Return a dateutil object from string [last update]
        originally in ISO 8601 format: YYYY-mm-ddTHH:MM:SS"""
        last_update = self.standings_json[self.standings_schedule_date]['standings_all_date_rptr']['standings_all_date'][0]['queryResults']['created']
        return dateutil.parser.parse(last_update)

    def parse_standings(self):
        """Parse the json standings"""
        sjson = self.standings_json[self.standings_schedule_date]['standings_all_date_rptr']['standings_all_date']
        for league in sjson:
            if league['league_id'] == '103':
                divisions = Standings.DIVISIONS['AL']
            elif league['league_id'] == '104':
                divisions = Standings.DIVISIONS['NL']
            else:
                # Raise Error
                try:
                    raise UnknownLeagueID('An unknown `league_id` was passed from standings json.')
                except UnknownLeagueID as e:
                    print 'StandingsError: ', e
                    raise
                    sys.exit(-1)

            for division in divisions:
                mlbdivision = []
                mlbdiv = type('Division', (object,), {'name': divisions[division]})
                teams = [team for team in league['queryResults']['row'] if team['division_id'] == division]
                for team in teams:
                    mlbteam = type('Team', (object,), team)
                    mlbdivision.append(mlbteam)
                setattr(mlbdiv, 'standings', mlbdivision)
                self.mlb_standings.append(mlbdiv)


class StandingsException(Exception):
    """Standings Exceptions"""


class UnknownLeagueID(StandingsException):
    """An unknown `league_id` was passed from standings json"""


#
# @meta_classes
#

#class Division(object):
#    """Represents an MLB Division in the standings
#
#    Properties:
#        name
#        teams
#    """

#class Team(object):
#    """Represents an MLB team in the standings"""
#
#    Properties:
#        streak
#        playoff_odds
#        elim
#        x_wl_seas
#        vs_right
#        gb
#        sit_code
#        home
#        last_ten
#        one_run
#        vs_division
#        playoff_points_sw
#        vs_left
#        is_wildcard_sw
#        vs_west
#        away
#        division_champ
#        pct
#        team_short
#        clinched_sw
#        playoffs_sw
#        playoffs_flag_mlb
#        division_id
#        division
#        interleague
#        playoffs_flag_milb
#        opp_runs
#        wild_card
#        elim_wildcard
#        x_wl
#        file_code
#        team_full
#        runs
#        wildcard_odds
#        vs_east
#        l
#        gb_wildcard
#        team_abbrev
#        points
#        place
#        w
#        division_odds
#        team_id
#        vs_central
#        extra_inn
#    """
