'''
This module maps stat indentifiers to what they most likely mean.
If there are blanks and you know what should go there, 
feel free to [submit an issue](https://github.com/zachpanz88/mlbgame/issues/new).

This module also provides what stat objects
will contain each property.
'''

'''
Stat identifiers and their meanings

`obj` - the objects that contain the stat

`always` - whether the stat is always present in those objects

`desc` - description of the stat
'''
idmap = {
    'name_display_first_last':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'desc': 'First and last name of player',
    },
    'name':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'desc': 'Abbreviated name, Either "F. Lastname" or "Lastname"',
    },
    'pos':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'desc': 'Player\'s position',
    },
    'id':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'desc': 'Player\'s id number for mlb.com',
    },
    'ab':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'At bats',
    },
    'avg':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'Batting average',
    },
    'h':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'desc': 'Hits (pitcher: given up)',
    },
    'r':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'desc': 'Runs (pitcher: given up)',
    },
    'rbi':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'Runs Batted In',
    },
    'hr':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'Home Runs',
    },
    'slg':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'Slugging percentage',
    },
    'obp':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'On base percentage',
    },
    'ops':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'On base (percentage) plus slugging (percentage)',
    },
    'fldg':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'Fielding percentage',
    },
    'bo':{
        'obj': ['BatterStats'],
        'always': True,
        'desc': 'Batting order',
    },
}