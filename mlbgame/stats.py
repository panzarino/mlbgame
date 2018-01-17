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
        # loops through pitchers
        for x in y.findall(name):
            stats = {}
            # loop through and save stats
            for i in x.attrib:
                stats[i] = x.attrib[i]
            # apply to correct list
            if y.attrib['team_flag'] == 'home':
                home.append(stats)
            elif not home:
                away.append(stats)
    return (home, away)


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
    # get parsed stats
    pitching_info = __player_stats_info(pitching, 'pitcher')
    batting_info = __player_stats_info(batting, 'batter')
    output = {
        'home_pitching': pitching_info[0],
        'away_pitching': pitching_info[1],
        'home_batting': batting_info[0],
        'away_batting': batting_info[1]
    }
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
        if x.attrib['team_flag'] == 'home':
            output['home_pitching'] = stats
        elif x.attrib['team_flag'] == 'away':
            output['away_pitching'] = stats
    # loop through pitching info
    for x in batting:
        stats = {}
        # loop through stats and save
        for y in x.attrib:
            stats[y] = x.attrib[y]
        # apply to correct team
        if x.attrib['team_flag'] == 'home':
            output['home_batting'] = stats
        elif x.attrib['team_flag'] == 'away':
            output['away_batting'] = stats
    return output


class Stats(object):
    """Hold stats information for a game.

    Properties:
        away_batting
        away_pitching
        game_id
        home_batting
        home_pitching
    """

    def __init__(self, data, game_id, player):
        """Creates a players object that matches the corresponding info in `data`.
        `data` should be an dictionary of values.
        'game_id' should be the id for the game.
        """
        self.game_id = game_id
        output = {'home_pitching': [], 'away_pitching': [], 'home_batting': [],
                  'away_batting': []}
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
