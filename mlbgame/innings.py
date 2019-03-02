#!/usr/bin/env python

"""Module that is used for getting the detailed events by inning
that occured throughout games.
"""

import mlbgame.data
import mlbgame.object
import mlbgame.events

import lxml.etree as etree


def game_innings(game_id):
    """Return dictionary of innings for a game with matching id."""
    # get data from data module
    data = mlbgame.data.get_innings(game_id)
    # parse XML
    parsed = etree.parse(data)
    root = parsed.getroot()
    # empty output file
    output = {}
    # loop through innings
    innings = root.findall('inning')
    for x in innings:
        output[x.attrib['num']] = {
            'top': mlbgame.events.__inning_info(x, 'top'),
            'bottom': mlbgame.events.__inning_info(x, 'bottom')
        }
    return output


class Inning(mlbgame.events.Inning):
    """ Class that inherits from events - Inning
    """

    def nice_output(self):
        """Prints basic inning info in a nice way."""
        return 'Inning {0}'.format(self.num)

    def __str__(self):
        return self.nice_output()


class AtBat(mlbgame.events.AtBat):
    """ Class that inherits from events - AtBat
    """

    def nice_output(self):
        """Prints basic at bat info in a nice way."""
        return self.des

    def __str__(self):
        return self.nice_output()


class Pitch(mlbgame.events.Pitch):
    """Class that inherits from events with more data

    Properties:
        des
        des_e
        id
        type
        code
        tfs
        tfs_zulu
        x
        y
        event_num
        sv_id
        play_guid
        start_speed
        end_speed
        sz_top
        sz_bot
        pfx_x
        pfx_z
        px
        pz
        x0
        y0
        z0
        vx0
        vy0
        vz0
        ax
        ay
        az
        break_y
        break_angle
        break_length
        pitch_type
        type_confidence
        zone
        nasty
        spin_dir
        spin_rate
        cc
        mt
    """

    def nice_output(self):
        """Prints basic event info in a nice way."""
        out = 'Pitch: {0} starting at {1}: ending at: {2} Description: {3}'
        return out.format(self.pitch_type, self.start_speed,
                          self.end_speed, self.des)

    def __str__(self):
        return self.nice_output()
