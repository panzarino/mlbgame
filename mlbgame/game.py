#!/usr/bin/env python

"""Module that is used for getting basic information about a game
such as the scoreboard and the box score.
"""

import datetime
import lxml.etree as etree

import mlbgame.data
import mlbgame.object


def scoreboard(year, month, day, home=None, away=None):
    """Return the scoreboard information for games matching the parameters
    as a dictionary.
    """
    # get data
    data = mlbgame.data.get_scoreboard(year, month, day)
    # parse data
    parsed = etree.parse(data)
    root = parsed.getroot()
    games = {}
    output = {}
    # loop through games
    for game in root:
        if game.tag == 'data':
            return []
        # get team names
        teams = game.findall('team')
        home_name = teams[0].attrib['name']
        away_name = teams[1].attrib['name']
        # check if teams match parameters
        if (home_name == home and home is not None) \
                or (away_name == away and away is not None) \
                or (away is None and home is None):
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
            if game_tag == 'go_game' or game_tag == 'ig_game':
                try:
                    w_pitcher_data = game.find('w_pitcher')
                    w_pitcher = w_pitcher_data.find('pitcher').attrib['name']
                    w_pitcher_wins = int(w_pitcher_data.attrib['wins'])
                    w_pitcher_losses = int(w_pitcher_data.attrib['losses'])
                except Exception:
                    w_pitcher = ""
                    w_pitcher_wins = 0
                    w_pitcher_losses = 0
                try:
                    l_pitcher_data = game.find('l_pitcher')
                    l_pitcher = l_pitcher_data.find('pitcher').attrib['name']
                    l_pitcher_wins = int(l_pitcher_data.attrib['wins'])
                    l_pitcher_losses = int(l_pitcher_data.attrib['losses'])
                except Exception:
                    l_pitcher = ""
                    l_pitcher_wins = 0
                    l_pitcher_losses = 0
                try:
                    sv_pitcher_data = game.find('sv_pitcher')
                    sv_pitcher = sv_pitcher_data.find('pitcher').attrib['name']
                    sv_pitcher_saves = int(sv_pitcher_data.attrib['saves'])
                except Exception:
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
            elif game_tag == 'sg_game':
                try:
                    p_pitcher_data = game.findall('p_pitcher')
                    p_pitcher_home_data = p_pitcher_data[0]
                    p_pitcher_home = p_pitcher_home_data.find(
                        'pitcher').attrib['name']
                    p_pitcher_home_wins = int(p_pitcher_home_data.
                                              attrib['wins'])
                    p_pitcher_home_losses = int(p_pitcher_home_data.
                                                attrib['losses'])
                    p_pitcher_away_data = p_pitcher_data[1]
                    p_pitcher_away = p_pitcher_away_data.find(
                        'pitcher').attrib['name']
                    p_pitcher_away_wins = int(p_pitcher_away_data.
                                              attrib['wins'])
                    p_pitcher_away_losses = int(p_pitcher_away_data.
                                                attrib['losses'])
                except Exception:
                    p_pitcher_home = ''
                    p_pitcher_home_wins = 0
                    p_pitcher_home_losses = 0
                    p_pitcher_away = ''
                    p_pitcher_away_wins = 0
                    p_pitcher_away_losses = 0
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
                    'p_pitcher_home': p_pitcher_home,
                    'p_pitcher_home_wins': p_pitcher_home_wins,
                    'p_pitcher_home_losses': p_pitcher_home_losses,
                    'p_pitcher_away': p_pitcher_away,
                    'p_pitcher_away_wins': p_pitcher_away_wins,
                    'p_pitcher_away_losses': p_pitcher_away_losses
                }
            # put this dictionary into the larger dictionary
            games[game_id] = output
    return games


class GameScoreboard(object):
    """Object to hold scoreboard information about a certain game.

    Properties:
        away_team
        away_team_errors
        away_team_hits
        away_team_runs
        date
        game_id
        game_league
        game_start_time
        game_status
        game_tag
        home_team
        home_team_errors
        home_team_hits
        home_team_runs
        l_pitcher
        l_pitcher_losses
        l_pitcher_wins
        l_team
        sv_pitcher
        sv_pitcher_saves
        w_pitcher
        w_pitcher_losses
        w_pitcher_wins
        w_team
    """

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
        # create a datetime object that represents the game start time
        # the object has no timezone info but should be interpreted as
        # being in the US/Eastern timezone
        year, month, day = self.game_id.split('_')[:3]
        game_start_date = "/".join([year, month, day])
        game_start_time = self.game_start_time.replace(' ', '')
        self.date = datetime.datetime.strptime(
                " ".join([game_start_date, game_start_time]),
                "%Y/%m/%d %I:%M%p")

    def nice_score(self):
        """Return a nicely formatted score of the game."""
        return ('{0.away_team} ({0.away_team_runs}) at '
                '{0.home_team} ({0.home_team_runs})').format(self)

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
    result = dict()
    result['game_id'] = game_id
    # loop through innings and add them to output
    for x in linescore:
        inning = x.attrib['inning']
        home = x.attrib['home']
        away = x.attrib['away']
        result[int(inning)] = {'home': home, 'away': away}
    return result


class GameBoxScore(object):
    """Object to hold the box score of a certain game.

    Properties:
        game_id
        innings:
            inning
            home
            away
    """

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
                result = {'inning': int(x),
                          'home': int(data[x]['home']),
                          'away': int(data[x]['away'])
                          }
            # possible error when 9th innning home team has 'x'
            # becuase they did not bat
            except ValueError:
                result = {
                    'inning': int(x),
                    'home': data[x]['home'],
                    'away': int(data[x]['away'])
                }
            self.innings.append(result)

    def __iter__(self):
        """Allows object to be iterated over."""
        for x in self.innings:
            yield x

    def __enumerate_scoreboard(self, data):
        output = ''
        for y, x in enumerate(data, start=1):
            if y >= 10:
                output += str(x) + '  '
            else:
                output += str(x) + ' '
        return output

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
        output += 'Inning\t'
        for x in innings:
            output += str(x) + ' '
        output += '\n'
        for x in innings:
            output += '---'
        output += '\nAway\t' + self.__enumerate_scoreboard(away)
        output += '\nHome\t' + self.__enumerate_scoreboard(home)
        return output


def overview(game_id):
    """Gets the overview information for the game with matching id."""
    # get data
    overview = mlbgame.data.get_overview(game_id)
    raw_box_score = mlbgame.data.get_raw_box_score(game_id)
    # parse data
    overview_root = etree.parse(overview).getroot()
    raw_box_score_root = etree.parse(raw_box_score).getroot()

    output = {}
    # get overview attributes
    for x in overview_root.attrib:
        output[x] = overview_root.attrib[x]
    # get raw box score attributes
    for x in raw_box_score_root.attrib:
        output[x] = raw_box_score_root.attrib[x]

    # Get probable starter attributes if they exist
    home_pitcher_tree = overview_root.find('home_probable_pitcher')
    if home_pitcher_tree is not None:
        output.update(build_namespaced_attributes(
            'home_probable_pitcher', home_pitcher_tree))
    else:
        output.update(build_probable_starter_defaults('home'))

    away_pitcher_tree = overview_root.find('away_probable_pitcher')
    if away_pitcher_tree is not None:
        output.update(build_namespaced_attributes(
            'away_probable_pitcher', away_pitcher_tree))
    else:
        output.update(build_probable_starter_defaults('away'))

    return output


def build_namespaced_attributes(name, tree):
    output = {}
    for attr in tree.attrib:
        output[name + '_' + attr] = tree.attrib[attr]
    return output


def build_probable_starter_defaults(name):
    output = {}
    output[name + '_probable_pitcher_era'] = ''
    output[name + '_probable_pitcher_first'] = ''
    output[name + '_probable_pitcher_first_name'] = ''
    output[name + '_probable_pitcher_id'] = ''
    output[name + '_probable_pitcher_last'] = ''
    output[name + '_probable_pitcher_last_name'] = ''
    output[name + '_probable_pitcher_losses'] = ''
    output[name + '_probable_pitcher_name_display_roster'] = ''
    output[name + '_probable_pitcher_number'] = ''
    output[name + '_probable_pitcher_s_era'] = ''
    output[name + '_probable_pitcher_s_losses'] = ''
    output[name + '_probable_pitcher_s_wins'] = ''
    output[name + '_probable_pitcher_stats_season'] = ''
    output[name + '_probable_pitcher_stats_type'] = ''
    output[name + '_probable_pitcher_throwinghand'] = ''
    output[name + '_probable_pitcher_wins'] = ''
    return output


class Overview(mlbgame.object.Object):
    """Object to hold an overview of game information

    Properties:
        ampm
        attendance
        aw_lg_ampm
        away_ampm
        away_code
        away_division
        away_file_code
        away_games_back
        away_games_back_wildcard
        away_league_id
        away_loss
        away_name_abbrev
        away_preview_link
        away_probable_pitcher_era
        away_probable_pitcher_first
        away_probable_pitcher_first_name
        away_probable_pitcher_id
        away_probable_pitcher_last
        away_probable_pitcher_last_name
        away_probable_pitcher_losses
        away_probable_pitcher_name_display_roster
        away_probable_pitcher_number
        away_probable_pitcher_s_era
        away_probable_pitcher_s_losses
        away_probable_pitcher_s_wins
        away_probable_pitcher_stats_season
        away_probable_pitcher_stats_type
        away_probable_pitcher_throwinghand
        away_probable_pitcher_wins
        away_recap_link
        away_sport_code
        away_team_city
        away_team_errors
        away_team_hits
        away_team_id
        away_team_name
        away_team_runs
        away_time
        away_time_zone
        away_win
        balls
        date
        day
        double_header_sw
        elapsed_time
        first_pitch_et
        game_data_directory
        game_id
        game_nbr
        game_pk
        game_type
        gameday_link
        gameday_sw
        hm_lg_ampm
        home_ampm
        home_code
        home_division
        home_file_code
        home_games_back
        home_games_back_wildcard
        home_league_id
        home_loss
        home_name_abbrev
        home_preview_link
        home_probable_pitcher_era
        home_probable_pitcher_first
        home_probable_pitcher_first_name
        home_probable_pitcher_id
        home_probable_pitcher_last
        home_probable_pitcher_last_name
        home_probable_pitcher_losses
        home_probable_pitcher_name_display_roster
        home_probable_pitcher_number
        home_probable_pitcher_s_era
        home_probable_pitcher_s_losses
        home_probable_pitcher_s_wins
        home_probable_pitcher_stats_season
        home_probable_pitcher_stats_type
        home_probable_pitcher_throwinghand
        home_probable_pitcher_wins
        home_recap_link
        home_sport_code
        home_team_city
        home_team_errors
        home_team_hits
        home_team_id
        home_team_name
        home_team_runs
        home_time
        home_time_zone
        home_win
        id
        ind
        inning
        inning_state
        is_no_hitter
        is_perfect_game
        league
        location
        note
        official_scorer
        original_date
        outs
        photos_link
        preview
        scheduled_innings
        start_time
        status
        status_ind
        strikes
        tbd_flag
        tiebreaker_sw
        time
        time_aw_lg
        time_date
        time_date_aw_lg
        time_date_hm_lg
        time_hm_lg
        time_zone
        time_zone_aw_lg
        time_zone_hm_lg
        top_inning
        tv_station
        tz_aw_lg_gen
        tz_hm_lg_gen
        venue
        venue_id
        venue_name
        venue_w_chan_loc
        weather
        wind
        wrapup_link
    """
    pass


def players(game_id):
    """Gets player/coach/umpire information for the game with matching id."""
    # get data
    data = mlbgame.data.get_players(game_id)
    # parse data
    parsed = etree.parse(data)
    root = parsed.getroot()

    output = {}
    output['game_id'] = game_id

    # get player/coach data
    for team in root.findall('team'):
        type = team.attrib['type'] + "_team"
        # the type is either home_team or away_team
        output[type] = {}
        output[type]['players'] = []
        output[type]['coaches'] = []

        for p in team.findall('player'):
            player = {}
            for key in p.keys():
                player[key] = p.get(key)
            output[type]['players'].append(player)

        for c in team.findall('coach'):
            coach = {}
            for key in c.keys():
                coach[key] = c.get(key)
            output[type]['coaches'].append(coach)

    # get umpire data
    output['umpires'] = []
    for u in root.find('umpires').findall('umpire'):
        umpire = {}
        for key in u.keys():
            umpire[key] = u.get(key)
        output['umpires'].append(umpire)

    return output


class Players(object):
    """Object to hold player/coach/umpire information for a game.

    Properties:
        away_coaches
        away_players
        game_id
        home_coaches
        home_players
        umpires
    """

    def __init__(self, data):
        """Creates a players object that matches the corresponding info in `data`.
        `data` should be an dictionary of values.
        """
        self.game_id = data['game_id']
        self.home_players = [Player(x) for x in data['home_team']['players']]
        self.home_coaches = [Coach(x) for x in data['home_team']['coaches']]
        self.away_players = [Player(x) for x in data['away_team']['players']]
        self.away_coaches = [Coach(x) for x in data['away_team']['coaches']]
        self.umpires = [Umpire(x) for x in data['umpires']]


class Player(mlbgame.object.Object):
    """Object to hold player information

    Properties:
        avg
        bats
        boxname
        current_position
        era
        first
        hr
        id
        last
        losses
        num
        parent_team_abbrev
        parent_team_id
        position
        rbi
        rl
        status
        team_abbrev
        team_id
        wins
    """
    pass


class Coach(mlbgame.object.Object):
    """Object to hold coach information

    Properties:
        first
        id
        last
        num
        position
    """
    pass


class Umpire(mlbgame.object.Object):
    """Object to hold umpire information

    Properties:
        first
        id
        last
        name
        position
    """
    pass
