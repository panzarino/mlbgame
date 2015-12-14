'''
This module maps stat indentifiers to what they most likely mean.
If there are blanks and you know what should go there, 
please [submit an issue](https://github.com/zachpanz88/mlbgame/issues/new) 
with the correct stat description.

This module also provides what stat objects
will contain each property.
'''

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
        'desc': 'Sacrifice (unknown if fly or bunt)',
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
}
'''
Stat identifiers and their meanings

`obj` - the objects that contain the stat

`always` - whether the stat is always present in those objects (None if unknown)

`type` - the value type of the stat

`desc` - description of the stat

Total season stats (stats prefixed with `s_`) for postseason games are total stats for that series only, 
not the entire season.

Assume that batting stats on a `PitcherStats` object are what he has given up.
Example: `hr` is home runs given up not home runs hit by that pitcher. 
Pitchers have their own `BatterStats` object for their own hitting stats.

If you are reading the documentation, 
you should click "show source" to see all the stat values
'''

batter_stats = {}
'''
The stats that appear in the BatterStats objects
'''
for x in idmap:
    for y in idmap[x]['obj']:
        if y == 'BatterStats':
            batter_stats[x] = idmap[x]