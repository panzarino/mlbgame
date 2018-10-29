#!/usr/bin/env python

"""Module that is used for getting the events
that occured throughout games.
"""

import lxml.etree as etree

import mlbgame.data
import mlbgame.object


class TagException(Exception):
    pass


def __inning_info(inning, part):
    # info
    info = []
    # loop through the half
    half = inning.findall(part)[0]
    for y in half.xpath('.//atbat | .//action'):
        atbat_action = {'tag': y.tag}
        # loop through and save info
        for i in y.attrib:
            atbat_action[i] = y.attrib[i]
        # only get pitches for atbat tags
        if y.tag == 'atbat':
            atbat_action['pitches'] = []
            for i in y.findall('pitch'):
                pitch = {}
                # loop through pitch info
                for n in i.attrib:
                    pitch[n] = i.attrib[n]
                atbat_action['pitches'].append(pitch)
        info.append(atbat_action)
    return info


def game_events(game_id):
    """Return dictionary of events for a game with matching id."""
    # get data from data module
    data = mlbgame.data.get_game_events(game_id)
    # parse XML
    parsed = etree.parse(data)
    root = parsed.getroot()
    # empty output file
    output = {}
    # loop through innings
    innings = root.findall('inning')
    for x in innings:
        output[x.attrib['num']] = {
            'top': __inning_info(x, 'top'),
            'bottom': __inning_info(x, 'bottom')
        }
    return output


class Inning(object):
    """Class that holds at bats in an inning.

    Properties:
        bottom
        num
        top
    """

    def __init__(self, data, inning):
        """Creates an inning object that matches the corresponding
        info in `data`.

        `data` should be a dictionary of values.
        """
        self.num = int(inning)
        self.top = []
        self.bottom = []

        for half, half_list in zip(['top', 'bottom'], [self.top, self.bottom]):
            for x in data[half]:
                if x['tag'] == 'atbat':
                    half_list.append(AtBat(x))
                elif x['tag'] == 'action':
                    half_list.append(Action(x))
                else:
                    raise TagException("Unknown event tag %s." % x['tag'])

    def nice_output(self):
        """Prints basic inning info in a nice way."""
        return 'Inning {0}'.format(self.num)

    def __str__(self):
        return self.nice_output()


class AtBat(object):
    """Class that holds information about at bats in games.

    Properties:
        away_team_runs
        b
        b1
        b2
        b3
        batter
        des
        des_es
        event
        event_es
        event_num
        home_team_runs
        num
        o
        pitcher
        pitches
        play_guid
        s
        start_tfs
        start_tfs_zulu
    """

    def __init__(self, data):
        """Creates an at bat object that matches the corresponding
        info in `data`.

        `data` should be a dictionary of values.
        """
        # loop through data
        for x in data:
            # create pitches list if attribute name is pitches
            if x == 'pitches':
                self.pitches = []
                for y in data[x]:
                    self.pitches.append(Pitch(y))
            else:
                # set information as correct data type
                mlbgame.object.setobjattr(self, x, data[x])

    def nice_output(self):
        """Prints basic at bat info in a nice way."""
        return self.des

    def __str__(self):
        return self.nice_output()


class Action(object):
    """Class that holds information about actions in games.

    Properties:
        away_team_runs
        b
        des
        des_es
        event
        event_es
        event_num
        home_team_runs
        o
        pitch
        player
        play_guid
        s
        tfs
        tfs_zulu
    """

    def __init__(self, data):
        """Creates an action object that matches the corresponding
        info in `data`.

        `data` should be a dictionary of values.
        """
        # add play_guid as it sometimes doesn't exist
        if 'play_guid' not in data:
            data['play_guid'] = ''
        # loop through data
        for x in data:
            # set information as correct data type
            mlbgame.object.setobjattr(self, x, data[x])

    def nice_output(self):
        """Prints basic at bat info in a nice way."""
        return self.des

    def __str__(self):
        return self.nice_output()


class Pitch(mlbgame.object.Object):
    """Class that holds information about individual pitches.

    Properties:
        des
        des_es
        pitch_type
        start_speed
        sv_id
        type
    """

    def nice_output(self):
        """Prints basic event info in a nice way."""
        return 'Pitch: {0} at {1}: {2}'.format(
            self.pitch_type, self.start_speed, self.des)

    def __str__(self):
        return self.nice_output()
