#!/usr/bin/env python

"""Module that is used for getting information
about the (MLB) league and the teams in it.
"""

from __future__ import print_function

import mlbgame.data
import mlbgame.object

from datetime import datetime
import dateutil.parser
import json
import lxml.etree as etree
import requests
import sys


def __get_league_object():
    """Returns the xml object corresponding to the league

    Only designed for internal use"""
    # get data
    data = mlbgame.data.get_properties()
    # return league object
    return etree.parse(data).getroot().find('leagues').find('league')


def league_info():
    """Returns a dictionary of league information"""
    league = __get_league_object()
    output = {}
    for x in league.attrib:
        output[x] = league.attrib[x]
    return output


def team_info():
    """Returns a list of team information dictionaries"""
    teams = __get_league_object().find('teams').findall('team')
    output = []
    for team in teams:
        info = {}
        for x in team.attrib:
            info[x] = team.attrib[x]
        output.append(info)
    return output


class Info(mlbgame.object.Object):
    """Holds information about the league or teams

    Properties:
        address
        aws_club_slug
        city
        club
        club_common_name
        club_common_url
        club_full_name
        club_id
        club_spanish_name
        country
        dc_site
        display_code
        division
        es_track_code
        esp_common_name
        esp_common_url
        facebook
        facebook_es
        fanphotos_url
        fb_app_id
        field
        google_tag_manager
        googleplus_id
        historical_team_code
        id
        instagram
        instagram_id
        league
        location
        medianet_id
        mobile_es_url
        mobile_short_code
        mobile_url
        mobile_url_base
        name_display_long
        name_display_short
        newsletter_category_id
        newsletter_group_id
        phone
        photostore_url
        pinterest
        pinterest_verification
        pressbox_title
        pressbox_url
        primary
        primary_link
        postal_code
        secondary
        shop_entry_code
        snapchat
        snapchat_es
        state_province
        team_code
        team_id
        tertiary
        timezone
        track_code
        track_code_dev
        track_filter
        tumblr
        twitter
        twitter_es
        url_cache
        url_esp
        url_prod
        venue_id
        vine
        youtube
    """

    def nice_output(self):
        """Return a string for printing"""
        return '{0} ({1})'.format(self.club_full_name, self.club.upper())

    def __str__(self):
        return self.nice_output()


def roster(team_id):
    """Returns a dictionary of roster information for team id"""
    data = mlbgame.data.get_roster(team_id)
    parsed = json.loads(data.read().decode('utf-8'))
    players = parsed['roster_40']['queryResults']['row']
    last_update = dateutil.parser.parse(
        parsed['roster_40']['queryResults']['created'])
    return {'players': players, 'last_update': last_update, 'team_id': team_id}


class Roster(object):
    """Represents an MLB Team

    Properties:
        last_update
        players
        team_id
    """

    def __init__(self, data):
        """Creates a roster object to match info in `data`.

        `data` should be a dictionary of values.
        """
        self.last_update = data['last_update']
        self.team_id = data['team_id']
        self.players = []
        for player in data['players']:
            self.players.append(Player(player))


class RosterException(Exception):
    """Roster Exceptions"""


class NoTeamID(RosterException):
    """A `team_id` was not supplied"""


class Player(mlbgame.object.Object):
    """Represents an MLB Player

    Properties:
        bats
        birth_date
        college
        end_date
        height_feet
        height_inches
        jersey_number
        name_display_first_last
        name_display_last_first
        name_first
        name_full
        name_last
        name_use
        player_id
        position_txt
        primary_position
        pro_debut_date
        start_date
        starter_sw
        status_code
        team_abbrev
        team_code
        team_id
        team_name
        throws
        weight
    """
    pass


def standings(date):
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
    now = datetime.now()
    divisions = []
    if date.year == now.year and date.month == now.month and date.day == now.day:
        data = mlbgame.data.get_standings(date)
        standings_schedule_date = 'standings_schedule_date'
    else:
        data = mlbgame.data.get_historical_standings(date)
        standings_schedule_date = 'historical_standings_schedule_date'
    parsed = json.loads(data.read().decode('utf-8'))
    last_update = parsed[standings_schedule_date][
            'standings_all_date_rptr']['standings_all_date'][0]['queryResults']['created']
    sjson = parsed[standings_schedule_date]['standings_all_date_rptr']['standings_all_date']
    for league in sjson:
        if league['league_id'] == '103':
            divs = DIVISIONS['AL']
        elif league['league_id'] == '104':
            divs = DIVISIONS['NL']
        for division in divs:
            teams = [team for team in league['queryResults']
                     ['row'] if team['division_id'] == division]
            divisions.append({
                'division': divs[division],
                'teams': teams
            })
    return {
        'standings_schedule_date': standings_schedule_date,
        'divisions': divisions,
        'last_update': dateutil.parser.parse(last_update)
    }


class Standings(object):
    """Holds information about the league standings

    Properties:
        divisions
        standings_schedule_date
        last_update
    """

    def __init__(self, data):
        self.standings_schedule_date = data['standings_schedule_date']
        self.last_update = data['last_update']
        self.divisions = [Division(x['division'], x['teams']) for x in data['divisions']]


class Division(object):
    """Represents an MLB Division in the standings

    Properties:
        name
        teams
    """

    def __init__(self, name, teams):
        self.name = name
        self.teams = []
        for team in teams:
            self.teams.append(Team(team))


class Team(mlbgame.object.Object):
    """Represents an MLB team in the standings

    Properties:
        away
        clinched_sw
        division
        division_champ
        division_id
        division_odds
        elim
        elim_wildcard
        extra_inn
        file_code
        gb
        gb_wildcard
        home
        interleague
        is_wildcard_sw
        l
        last_ten
        one_run
        opp_runs
        pct
        place
        playoff_odds
        playoff_points_sw
        playoffs_flag_milb
        playoffs_flag_mlb
        playoffs_sw
        points
        runs
        sit_code
        streak
        team_abbrev
        team_full
        team_id
        team_short
        vs_central
        vs_division
        vs_east
        vs_left
        vs_right
        vs_west
        w
        wild_card
        wildcard_odds
        x_wl
        x_wl_seas
    """
    pass


class Injuries(object):
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
            self.last_update = self.set_last_update()
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
            return requests.get(Injuries.injury_url).json()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(-1)

    def set_last_update(self):
        """Return a dateutil object from string [last update]
        originally in ISO 8601 format: YYYY-mm-ddTHH:MM:SS"""
        last_update = self.injury_json['wsfb_news_injury']['queryResults']['created']
        return dateutil.parser.parse(last_update)

    def parse_injury(self):
        """Parse the json injury"""
        injuries = self.injury_json['wsfb_news_injury']['queryResults']['row']
        injuries = [
            injury for injury in injuries if injury['team_id'] == self.team_id]
        for injury in injuries:
            mlbinjury = Injury(injury)
            self.injuries.append(mlbinjury)


class injuryException(Exception):
    """injury Exceptions"""


class TeamIDException(injuryException):
    """A `team_id` was not supplied or the `team_id` was not an integer."""


class Injury(mlbgame.object.Object):
    """Represents an MLB injury

    Properties:
        display_ts
        due_back
        injury_desc
        injury_status
        injury_update
        insert_ts
        league_id
        name_first
        name_last
        player_id
        position
        team_id
        team_name
    """
    pass
