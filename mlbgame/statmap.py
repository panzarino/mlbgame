#!/usr/bin/env python

"""This module maps stat indentifiers to what they most likely mean.
If there are blanks and you know what should go there,
or there is a missing stat identifier, 
please [submit an issue](https://github.com/zachpanz88/mlbgame/issues/new) 
with the correct stat and description.

This module also provides what stat objects
will contain each property.
"""

# full idmap description at bottom of file
idmap = {
    'name_display_first_last':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': str,
        'desc': 'First and last name of player',
    },
    'name':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': str,
        'desc': 'Abbreviated name, Either "F. Lastname" or "Lastname"',
    },
    'pos':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': str,
        'desc': 'Player\'s position',
    },
    'id':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Player\'s id number for mlb.com',
    },
    'ab':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'At bats',
    },
    'avg':{
        'obj': ['BatterStats'],
        'always': True,
        'type': float,
        'desc': 'Batting average',
    },
    'h':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Hits',
    },
    'd':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Doubles',
    },
    't':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Triples',
    },
    'r':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'tpye': int,
        'desc': 'Runs',
    },
    'rbi':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Runs Batted In',
    },
    'hr':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Home runs',
    },
    'slg':{
        'obj': ['BatterStats'],
        'always': False,
        'type': float,
        'desc': 'Slugging percentage. '
                'Always availible in regular '
                'and postseason games.',
    },
    'obp':{
        'obj': ['BatterStats'],
        'always': True,
        'type': float,
        'desc': 'On base percentage',
    },
    'ops':{
        'obj': ['BatterStats'],
        'always': False,
        'type': float,
        'desc': 'On base (percentage) plus slugging (percentage) '
                'Always availible in regular '
                'and postseason games.',
    },
    'fldg':{
        'obj': ['BatterStats'],
        'always': True,
        'type': float,
        'desc': 'Fielding percentage',
    },
    'bo':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Position in batting order. '
                'A number divisible by 100 indicates the starter '
                'and every increase by one indicates that the player was the '
                'next player to bat in that position in the order '
                'ex. 401 means the second player in the game to bat in the fourth position.',
    },
    'bb':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Base on balls (walk)',
    },
    'sb':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Stolen bases',
    },
    'cs':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Caught stealing',
    },
    'e':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Errors (fielding)',
    },
    'hpb':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Hit by pitch',
    },
    'so':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Strikeouts',
    },
    'sac':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Sacrifice bunts',
    },
    'sf':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Sacrifice flies',
    },
    'lob':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Left on base',
    },
    'ao':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Fly outs',
    },
    'po':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Putouts (fielding)',
    },
    'a':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Assists (fielding)',
    },
    'go':{
        'obj': ['BatterStats'],
        'always': False,
        'type': int,
        'desc': 'Ground outs',
    },
    's_h':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Total season hits',
    },
    's_r':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Total season runs',
    },
    's_hr':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Total season home runs',
    },
    's_rbi':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Total season runs batted in',
    },
    's_so':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Total season strikeouts',
    },
    's_bb':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Total season base on balls (walks)',
    },
    'l':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Losses',
    },
    'w':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Wins',
    },
    'sv':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Saves',
    },
    'er':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Earned runs',
    },
    'hld':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Hold',
    },
    'bs':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Blown saves',
    },
    'out':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Outs recorded',
    },
    'bf':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Batters faced',
    },
    'game_score':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Game score: '
                'A metric to determine the stength '
                'of a pitcher in any baseball game. '
                'More info: https://en.wikipedia.org/wiki/Game_score',
    },
    'era':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': float,
        'desc': 'Earned runs average',
    },
    'np':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Number of pitches thrown '
                '(pitch count)',
    },
    'win':{
        'obj': ['PitcherStats'],
        'always': False,
        'type': str,
        'desc': 'The pitcher got the win for this game '
                'if set to true',
    },
    'loss':{
        'obj': ['PitcherStats'],
        'always': False,
        'type': str,
        'desc': 'The pitcher got the loss for this game '
                'if set to true',
    },
    'save':{
        'obj': ['PitcherStats'],
        'always': False,
        'type': str,
        'desc': 'The pitcher got the save for this game '
                'if set to true',
    },
    'note':{
        'obj': ['PitcherStats'],
        'always': False,
        'type': str,
        'desc': 'Extra information about a pitcher',
    },
    's_er':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Season earned runs',
    },
    's_ip':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Season innings pitched',
    },
    's':{
        'obj': ['PitcherStats'],
        'always': True,
        'type': int,
        'desc': 'Unknown',
    },
}
"""Stat identifiers and their meanings

`obj` - the objects that contain the stat

`always` - whether the stat is always present in those objects (None if unknown)

`type` - the value type of the stat

`desc` - description of the stat

Total season stats (stats prefixed with `s_`) for postseason games are total stats for that series only, 
not the entire season. If it is a preseason game, it is cumulative stats for that preseason.

Assume that batting stats on a `PitcherStats` object are what he has given up.
Example: `hr` is home runs given up not home runs hit by that pitcher. 
Pitchers have their own `BatterStats` object for their own hitting stats.

If you are reading the documentation, 
you should click "show source" to see all the stat values.

Some official stat abbreviations on 
[mlb.com](http://mlb.mlb.com/mlb/official_info/baseball_basics/abbreviations.jsp)
"""
