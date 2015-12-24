'''
Module that controls getting stats 
and creating objects to hold that information.
'''

import lxml.etree as etree
import mlbgame.data

def player_stats(game_id):
    '''
    Return individual stats of a game with matching id
    '''
    data = mlbgame.data.get_box_score(game_id)
    parsed = etree.parse(data)
    root = parsed.getroot()
    pitching = root.findall('pitching')
    batting = root.findall('batting')
    home_pitching = []
    away_pitching = []
    home_batting = []
    away_batting = []
    for y in pitching:
        home=False
        if y.attrib['team_flag'] == "home":
            home = True
        for x in y.findall('pitcher'):
            stats = {}
            for i in x.attrib:
                stats[i]=x.attrib[i]
            if home:
                home_pitching.append(stats)
            elif not home:
                away_pitching.append(stats)
    for y in batting:
        home=False
        if y.attrib['team_flag'] == "home":
            home = True
        for x in y.findall('batter'):
            stats = {}
            for i in x.attrib:
                stats[i]=x.attrib[i]
            if home:
                home_batting.append(stats)
            elif not home:
                away_batting.append(stats)
    output = {'home_pitching':home_pitching, 'away_pitching':away_pitching, 'home_batting':home_batting, 'away_batting':away_batting}
    return output

def team_stats(game_id):
    '''
    Return team stats of a game with matching id
    '''
    data = mlbgame.data.get_box_score(game_id)
    parsed = etree.parse(data)
    root = parsed.getroot()
    pitching = root.findall('pitching')
    batting = root.findall('batting')
    output = {}
    for x in pitching:
        stats = {}
        if x.attrib['team_flag']=='home':
            for y in x.attrib:
                stats[y] = x.attrib[y]
            output['home_pitching']=stats
        elif x.attrib['team_flag']=='away':
            for y in x.attrib:
                stats[y] = x.attrib[y]
            output['away_pitching']=stats
    for x in batting:
        stats = {}
        if x.attrib['team_flag']=='home':
            for y in x.attrib:
                stats[y] = x.attrib[y]
            output['home_batting']=stats
        elif x.attrib['team_flag']=='away':
            for y in x.attrib:
                stats[y] = x.attrib[y]
            output['away_batting']=stats
    return output

class Stats(object):
    '''
    Basic stats class for any type of stats
    '''
    
    def __init__(self, data):
        '''
        Creates a stats object that matches the corresponding stats in `data`
        
        `data` should be an dictionary of values
        '''
        for x in data:
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    try:
                        setattr(self, x, bool(data[x]))
                    except ValueError:
                        setattr(self, x, str(data[x]))

class PitcherStats(Stats):
    '''
    Holds stats information for a pitcher
    
    Check out `statmap.py` for a full list of object properties
    '''

    def nice_output(self):
        '''
        Prints basic pitcher stats in a nice way
        '''
        return "%s - %i Earned Runs, %i Strikouts, %i Hits" % (self.name_display_first_last, self.er, self.so, self.h)
    
    def __str__(self):
        return self.nice_output()

class BatterStats(Stats):
    '''
    Holds stats information for a batter
    
    Check out `statmap.py` for a full list of object properties
    '''
    
    def nice_output(self):
        '''
        Prints basic batter stats in a nice way
        '''
        if self.rbi > 0:
            if self.hr > 0:
                return "%s - %i for %i with %i RBI and %i Home Runs" % (self.name_display_first_last, self.h, self.ab, self.rbi, self.hr)
            return "%s - %i for %i with %i RBI" % (self.name_display_first_last, self.h, self.ab, self.rbi)
        return "%s - %i for %i" % (self.name_display_first_last, self.h, self.ab)
    
    def __str__(self):
        return self.nice_output()

class TeamStats(Stats):
    '''
    Holds total pitching stats for a team
    '''
    pass