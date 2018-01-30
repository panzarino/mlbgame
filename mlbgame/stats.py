#!/usr/bin/env python

"""Module that controls getting stats and creating objects to hold that
information."""

import mlbgame.data
import mlbgame.object

import lxml.etree as etree

def __player_stats_info(data, name):
    home = []
    away = []
    for y in data:
        # loops through pitchers and batters
        for x in y.findall(name):
            stats = {}
            # loop through and save stats
            for i in x.attrib:
                stats[i] = x.attrib[i]
            # apply to correct list
            home.append(stats) if y.attrib['team_flag'] == 'home' else away.append(stats)
    return (home, away)

def __raw_player_stats_info(data):
    home_pitchers = []
    away_pitchers = []
    home_batters = []
    away_batters = []

    for team in data.findall('team'):
        home_flag = team.attrib['team_flag'] == 'home'
        pitching = team.find('pitching')
        for pitcher in pitching.findall('pitcher'):
            stats = {}
            for i in pitcher.attrib:
                stats[i] = pitcher.attrib[i]
            home_pitchers.append(stats) if home_flag else away_pitchers.append(stats)

        batting = team.find('batting')
        for batter in batting.findall('batter'):
            stats = {}
            for i in batter.attrib:
                stats[i] = batter.attrib[i]
            home_batters.append(stats) if home_flag else away_batters.append(stats)
    home = {
        'pitchers': home_pitchers,
        'batters': home_batters
    }

    away = {
        'pitchers': away_pitchers,
        'batters': away_batters
    }
    return (home, away)

def player_stats(game_id):
    """Return dictionary of individual stats of a game with matching id.

       The additional pitching/batting is mostly the same stats, except it contains
       some useful stats such as groundouts/flyouts per pitcher (go/ao). MLB decided
       to have two box score files, thus we return the data from both.
    """
    # get data from data module
    box_score = mlbgame.data.get_box_score(game_id)
    raw_box_score = mlbgame.data.get_raw_box_score(game_id)
    # parse XML
    box_score_tree = etree.parse(box_score).getroot()
    raw_box_score_tree = etree.parse(raw_box_score).getroot()
    # get pitching and batting info
    pitching = box_score_tree.findall('pitching')
    batting = box_score_tree.findall('batting')
    # get parsed stats
    pitching_info = __player_stats_info(pitching, 'pitcher')
    batting_info = __player_stats_info(batting, 'batter')
    # get parsed additional stats
    additional_stats = __raw_player_stats_info(raw_box_score_tree)
    addl_home_pitching = additional_stats[0]['pitchers']
    addl_home_batting = additional_stats[0]['batters']
    addl_away_pitching = additional_stats[1]['pitchers']
    addl_away_batting = additional_stats[1]['batters']

    output = {
        'home_pitching': pitching_info[0],
        'away_pitching': pitching_info[1],
        'home_batting': batting_info[0],
        'away_batting': batting_info[1],
        'home_additional_pitching': addl_home_pitching,
        'away_additional_pitching': addl_away_pitching,
        'home_additional_batting': addl_home_batting,
        'away_additional_batting': addl_away_batting
    }
    return output

def __team_stats_info(data, output, output_key):
    for x in data:
        stats = {}
        # loop through stats and save
        for y in x.attrib:
            stats[y] = x.attrib[y]
        # apply to correct team
        if x.attrib['team_flag'] == 'home':
            # Example: 'home_batting' when output_key is 'batting'
            output['home_' + output_key] = stats
        elif x.attrib['team_flag'] == 'away':
            output['away_' + output_key] = stats
    return output

def __raw_team_stats_info(data, output):
    for team in data.findall('team'):
        home_flag = team.attrib['team_flag'] == 'home'
        pitching = team.find('pitching')
        stats = {}
        for stat in pitching.attrib:
            stats[stat] = pitching.attrib[stat]
        if home_flag:
            output['home_additional_pitching'] = stats
        else:
            output['away_additional_pitching'] = stats

        stats = {}
        batting = team.find('batting')
        for stat in batting.attrib:
            stats[stat] = batting.attrib[stat]
        if home_flag:
            output['home_additional_batting'] = stats
        else:
            output['away_additional_batting'] = stats
    return output

def team_stats(game_id):
    """Return team stats of a game with matching id.

    The additional pitching/batting is mostly the same stats. MLB decided
    to have two box score files, thus we return the data from both.
    """
    # get data from data module
    box_score = mlbgame.data.get_box_score(game_id)
    raw_box_score = mlbgame.data.get_raw_box_score(game_id)
    # parse XML
    box_score_tree = etree.parse(box_score).getroot()
    raw_box_score_tree = etree.parse(raw_box_score).getroot()
    # get pitching and batting ingo
    pitching = box_score_tree.findall('pitching')
    batting = box_score_tree.findall('batting')
    # dictionary for output
    output = {}
    output = __team_stats_info(pitching, output, 'pitching')
    output = __team_stats_info(batting, output, 'batting')
    output = __raw_team_stats_info(raw_box_score_tree, output)
    return output

class Stats(object):
    """Hold stats information for a game.

    Properties:
        away_batting
        away_pitching
        game_id
        home_batting
        home_pitching
        away_additional_pitching
        away_additional_batting
        home_additional_pitching
        home_additional_batting
    """

    def __init__(self, data, game_id, player):
        """Creates a players object that matches the corresponding info in `data`.
        `data` should be an dictionary of values.
        'game_id' should be the id for the game.
        """
        self.game_id = game_id
        output = {'home_pitching': [], 'away_pitching': [], 'home_batting': [],
                  'away_batting': [], 'home_additional_pitching': [], 'home_additional_batting': [],
                  'away_additional_pitching': [], 'away_additional_batting': []}
        for y in data:
            # create objects for all data
            if player:
                for x in data[y]:
                    obj = PlayerStats(x)
                    output[y].append(obj)
            else:
                obj = TeamStats(data[y])
                output[y] = obj
        self.home_pitching = output['home_pitching']
        self.away_pitching = output['away_pitching']
        self.home_batting = output['home_batting']
        self.away_batting = output['away_batting']
        self.home_additional_pitching = output['home_additional_pitching']
        self.away_additional_pitching = output['away_additional_pitching']
        self.home_additional_batting = output['home_additional_batting']
        self.away_additional_batting = output['away_additional_batting']

class PlayerStats(mlbgame.object.Object):
    """Holds stats information for a player.
    Properties:
        Batter:
            a
            ab
            ao
            avg
            bb
            bo
            cs
            d
            e
            fldg
            go
            h
            hbp
            hr
            id
            lob
            name
            name_display_first_last
            obp
            ops
            po
            pos
            r
            rbi
            s_bb
            s_h
            s_hr
            s_r
            s_rbi
            s_so
            sac
            sb
            sf
            slg
            so
            t
        Pitcher:
            bb
            bf
            bs
            er
            era
            game_score
            h
            hld
            hr
            id
            l
            loss
            name
            name_display_first_last
            note
            np
            out
            pos
            r
            s
            s_bb
            s_er
            s_h
            s_ip
            s_r
            s_so
            save
            so
            sv
            w
            win
    """

    def nice_output(self):
        """Prints basic player stats in a nice way."""
        return '{0} ({1})'.format(
            self.name_display_first_last,
            self.pos
        )

    def __str__(self):
        return self.nice_output()


class TeamStats(mlbgame.object.Object):
    """Holds total pitching or batting stats for a team.

    Properties:
        Batting:
            ab
            avg
            bb
            d
            da
            h
            hr
            lob
            obp
            ops
            po
            r
            rbi
            slg
            so
            t
            team_flag
        Pitching:
            bb
            bf
            er
            era
            h
            hr
            out
            r
            so
            team_flag
    """
    pass
