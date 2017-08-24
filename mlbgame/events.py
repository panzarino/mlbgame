#!/usr/bin/env python

"""Module that is used for getting the events
that occured throughout games.
"""

import mlbgame.data

import lxml.etree as etree


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
        # top info
        topinfo = []
        # loop through the top half
        top = x.findall('top')[0]
        for y in top.findall('atbat'):
            atbat = {}
            # loop through and save info
            for i in y.attrib:
                atbat[i] = y.attrib[i]
            atbat['pitches'] = []
            for i in y.findall('pitch'):
                pitch = {}
                # loop through pitch info
                for n in i.attrib:
                    pitch[n] = i.attrib[n]
                atbat['pitches'].append(pitch)
            topinfo.append(atbat)
        # bottom info
        botinfo = []
        # loop through the bottom half
        bot = x.findall('bottom')[0]
        for y in bot.findall('atbat'):
            atbat = {}
            # loop through and save info
            for i in y.attrib:
                atbat[i] = y.attrib[i]
            atbat['pitches'] = []
            for i in y.findall('pitch'):
                pitch = {}
                # loop through pitch info
                for n in i.attrib:
                    pitch[n] = i.attrib[n]
                atbat['pitches'].append(pitch)
            botinfo.append(atbat)
        output[x.attrib['num']] = {'top': topinfo, 'bottom': botinfo}
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
        self.num = inning
        self.top = [AtBat(x) for x in data['top']]
        self.bottom = [AtBat(x) for x in data['bottom']]

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
        event
        event_num
        home_team_runs
        num
        o
        pitcher
        pitches
        s
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
                continue
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    try:
                        setattr(self, x, str(data[x]))
                    except UnicodeEncodeError:
                        setattr(self, x, data[x])

    def nice_output(self):
        """Prints basic at bat info in a nice way."""
        return self.des

    def __str__(self):
        return self.nice_output()


class Pitch(object):
    """Class that holds information about individual pitches.

    Properties:
        des
        pitch_type
        start_speed
        sv_id
        type
    """

    def __init__(self, data):
        """Creates a pitch object that matches the corresponding info in `data`.

        `data` should be a dictionary of values.
        """
        # loop through data
        for x in data:
            # remove spanish info (causes text encoding errors)
            if '_es' in x:
                continue
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    setattr(self, x, str(data[x]))

    def nice_output(self):
        """Prints basic event info in a nice way."""
        return 'Pitch: {0} at {1}: {2}'.format(
            self.pitch_type, self.start_speed, self.des)

    def __str__(self):
        return self.nice_output()
