#!/usr/bin/env python

"""Module that is used for getting basic information about a game 
such as the scoreboard and the box score.
"""

import mlbgame.data

import datetime
import lxml.etree as etree

def scoreboard(year, month, day, home=None, away=None):
    """Return the scoreboard information for games matching the parameters as a dictionary."""
    # get data
    data = mlbgame.data.get_scoreboard(year, month, day)
    # parse data
    parsed = etree.parse(data)
    root = parsed.getroot()
    games = {}
    # loop through games
    for game in root:
        if game.tag == "data":
            return []
        # get team names
        teams = game.findall('team')
        home_name = teams[0].attrib['name']
        away_name = teams[1].attrib['name']
        # check if teams match parameters
        if (home_name == home and home!=None) or (away_name == away and away!=None) or (away==None and home==None):
            # throw all the data into a complicated dictionary
            game_tag = game.tag
            game_data = game.find('game')
            game_id = game_data.attrib['id']
            game_league = game_data.attrib['league']
            game_status = game_data.attrib['status']
            game_start_time = game_data.attrib['start_time']
            home_team_data = teams[0].find('gameteam')
            home_team = home_name
            home_team_runs = int(home_team_data.attrib['R'])
            home_team_hits = int(home_team_data.attrib['H'])
            home_team_errors = int(home_team_data.attrib['E'])
            away_team_data = teams[1].find('gameteam')
            away_team = away_name
            away_team_runs = int(away_team_data.attrib['R'])
            away_team_hits = int(away_team_data.attrib['H'])
            away_team_errors = int(away_team_data.attrib['E'])
            # check type of game
            if game_tag == "go_game" or game_tag == "ig_game":
                try:
                    w_pitcher_data = game.find('w_pitcher')
                    w_pitcher = w_pitcher_data.find('pitcher').attrib['name']
                    w_pitcher_wins = int(w_pitcher_data.attrib['wins'])
                    w_pitcher_losses = int(w_pitcher_data.attrib['losses'])
                except:
                    w_pitcher = ""
                    w_pitcher_wins = 0
                    w_pitcher_losses = 0
                try:
                    l_pitcher_data = game.find('l_pitcher')
                    l_pitcher = l_pitcher_data.find('pitcher').attrib['name']
                    l_pitcher_wins = int(l_pitcher_data.attrib['wins'])
                    l_pitcher_losses = int(l_pitcher_data.attrib['losses'])
                except:
                    l_pitcher = ""
                    l_pitcher_wins = 0
                    l_pitcher_losses = 0
                try:
                    sv_pitcher_data = game.find('sv_pitcher')
                    sv_pitcher = sv_pitcher_data.find('pitcher').attrib['name']
                    sv_pitcher_saves = int(sv_pitcher_data.attrib['saves'])
                except:
                    sv_pitcher = ""
                    sv_pitcher_saves = 0
                output = {
                    'game_id': game_id,
                    'game_tag': game_tag,
                    'game_league': game_league,
                    'game_status': game_status,
                    'game_start_time': game_start_time,
                    'home_team': home_team,
                    'home_team_runs': home_team_runs,
                    'home_team_hits': home_team_hits,
                    'home_team_errors': home_team_errors,
                    'away_team': away_team,
                    'away_team_runs': away_team_runs,
                    'away_team_hits': away_team_hits,
                    'away_team_errors': away_team_errors,
                    'w_pitcher': w_pitcher,
                    'w_pitcher_wins': w_pitcher_wins,
                    'w_pitcher_losses': w_pitcher_losses,
                    'l_pitcher': l_pitcher,
                    'l_pitcher_wins': l_pitcher_wins,
                    'l_pitcher_losses': l_pitcher_losses,
                    'sv_pitcher': sv_pitcher,
                    'sv_pitcher_saves': sv_pitcher_saves
                }
            # games that were not played
            elif game_tag == "sg_game":
                try:
                    p_pitcher_data = game.findall('p_pitcher')
                    p_pitcher_home_data = p_pitcher_data[0]
                    p_pitcher_home = p_pitcher_home_data.find('pitcher').attrib['name']
                    p_pitcher_home_wins = int(p_pitcher_home_data.attrib['wins'])
                    p_pitcher_home_losses = int(p_pitcher_home_data.attrib['losses'])
                    p_pitcher_away_data = p_pitcher_data[1]
                    p_pitcher_away = p_pitcher_away_data.find('pitcher').attrib['name']
                    p_pitcher_away_wins = int(p_pitcher_away_data.attrib['wins'])
                    p_pitcher_away_losses = int(p_pitcher_away_data.attrib['losses'])
                except:
                    p_pitcher_home = ""
                    p_pitcher_home_wins = 0
                    p_pitcher_home_losses = 0
                    p_pitcher_away = ""
                    p_pitcher_away_wins = 0
                    p_pitcher_away_losses = 0
                output = {
                    'game_id':game_id,
                    'game_tag':game_tag,
                    'game_league':game_league,
                    'game_status':game_status,
                    'game_start_time':game_start_time,
                    'home_team':home_team,
                    'home_team_runs': home_team_runs,
                    'home_team_hits': home_team_hits,
                    'home_team_errors': home_team_errors,
                    'away_team':away_team,
                    'away_team_runs': away_team_runs,
                    'away_team_hits': away_team_hits,
                    'away_team_errors': away_team_errors,
                    'p_pitcher_home':p_pitcher_home,
                    'p_pitcher_home_wins': p_pitcher_home_wins,
                    'p_pitcher_home_losses': p_pitcher_home_losses,
                    'p_pitcher_away':p_pitcher_away,
                    'p_pitcher_away_wins': p_pitcher_away_wins,
                    'p_pitcher_away_losses': p_pitcher_away_losses
                }
            # put this dictionary into the larger dictionary
            games[game_id]=output
    return games

class GameScoreboard(object):
    """Object to hold scoreboard information about a certain game."""
    
    def __init__(self, data):
        """Creates a `GameScoreboard` object.

        data is expected to come from the `scoreboard()` function.
        """
        # loop through data
        for x in data:
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    setattr(self, x, str(data[x]))
        # calculate the winning team
        if self.home_team_runs > self.away_team_runs:
            self.w_team = self.home_team
            self.l_team = self.away_team
        elif self.away_team_runs > self.home_team_runs:
            self.w_team = self.away_team
            self.l_team = self.home_team
        # create the datetime object for the game
        year, month, day, rest = self.game_id.split('_', 3)
        hour, other = self.game_start_time.split(':', 2)
        minute = other[:2]
        am_pm = other[2:]
        if am_pm == "PM":
            hour = int(hour)+11
        self.date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    
    def nice_score(self):
        """Return a nicely formatted score of the game."""
        return '%s (%d) at %s (%d)' % (self.away_team, self.away_team_runs, self.home_team, self.home_team_runs)
    
    def __str__(self):
        return self.nice_score()

def box_score(game_id):
    """Gets the box score information for the game with matching id."""
    # get data
    data = mlbgame.data.get_box_score(game_id)
    # parse data
    parsed = etree.parse(data)
    root = parsed.getroot()
    linescore = root.find('linescore')
    result = {}
    result['game_id']=game_id
    # loop through innings and add them to output
    for x in linescore:
        inning = x.attrib['inning']
        home = x.attrib['home']
        away = x.attrib['away']
        result[int(inning)] = {'home':home, 'away':away}
    return result

class GameBoxScore(object):
    """Object to hold the box score of a certain game."""
    
    def __init__(self, data):
        """Creates a `GameBoxScore` object.

        data is expected to come from the `box_score()` function.
        """
        self.game_id = data['game_id']
        data.pop('game_id', None)
        # dictionary of innings
        self.innings = []
        # loops through the innings
        for x in sorted(data):
            try:
                result = {'inning':int(x), 'home':int(data[x]['home']), 'away':int(data[x]['away'])}
            # possible error when 9th innning home team has 'x' becuase they did not bat
            except ValueError:
                result = {'inning':int(x), 'home':data[x]['home'], 'away':int(data[x]['away'])}
            self.innings.append(result)
    
    def __iter__(self):
        """Allows object to be iterated over."""
        for x in self.innings:
            yield x
    
    def print_scoreboard(self):
        """Print object as a scoreboard."""
        output = ''
        # parallel dictionaries with innings and scores
        innings = []
        away = []
        home = []
        for x in self:
            innings.append(x['inning'])
            away.append(x['away'])
            home.append(x['home'])
        # go through all the information and make a nice output
        # that looks like a scoreboard
        output += "Inning\t"
        for x in innings:
            output += str(x)+" "
        output += '\n'
        for x in innings:
            output += "---"
        output += "\nAway\t"
        for y, x in enumerate(away, start=1):
            if y>=10:
                output += str(x)+"  "
            else:
                output += str(x)+" "
        output += "\nHome\t"
        for y, x in enumerate(home, start=1):
            if y>=10:
                output += str(x)+"  "
            else:
                output += str(x)+" "
        return output

def overview(game_id):
    """Gets the overview information for the game with matching id."""
    # get data
    data = mlbgame.data.get_overview(game_id)
    # parse data
    parsed = etree.parse(data)
    root = parsed.getroot()
    output = {}
    # get overview attributes
    for x in root.attrib:
        output[x] = root.attrib[x]
    return output

class Overview(object):
    """Object to hold an overview of game information
    
    `elements` property is a set of all properties that an object contains.
    """
    
    def __init__(self, data):
        """Creates an overview object that matches the corresponding info in `data`.
        
        `data` should be an dictionary of values.
        """
        element_list = []
        # loop through data
        for x in data:
            # set information as correct data type
            try:
                setattr(self, x, int(data[x]))
            except ValueError:
                try:
                    setattr(self, x, float(data[x]))
                except ValueError:
                    # string if not number
                    setattr(self, x, str(data[x]))
            element_list.append(x)
        self.elements = set(element_list)