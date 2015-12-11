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

`always` - whether the stat is always present in those objects (None if unknown)

`type` - the value type of the stat

`desc` - description of the stat
'''
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
        'desc': 'Hits (pitcher: given up)',
    },
    'r':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'tpye': int,
        'desc': 'Runs (pitcher: given up)',
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
        'desc': 'Home Runs (pitcher: given up)',
    },
    'slg':{
        'obj': ['BatterStats'],
        'always': True,
        'type': float,
        'desc': 'Slugging percentage',
    },
    'obp':{
        'obj': ['BatterStats'],
        'always': True,
        'type': float,
        'desc': 'On base percentage',
    },
    'ops':{
        'obj': ['BatterStats'],
        'always': True,
        'type': float,
        'desc': 'On base (percentage) plus slugging (percentage)',
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
        'desc': 'Position in batting order',
    },
    'bb':{
        'obj': ['PitcherStats', 'BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Base on balls (aka. walk) (pitcher: given up)',
    },
    'sb':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Strolen bases',
    },
    'e':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Errors',
    },
    'hpb':{
        'obj': ['BatterStats'],
        'always': True,
        'type': int,
        'desc': 'Hit by pitch',
    },
}