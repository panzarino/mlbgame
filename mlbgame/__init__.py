#!/usr/bin/env python

"""mlbgame is a Python API to retrieve and read
MLB GameDay data.
mlbgame works with real time data, getting information as games are
being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame [documentation](http://panz.io/mlbgame)

mlbgame on [Github](https://github.com/panzarino/mlbgame) (Source Code)

If you have a question or need help, the quickest way to get a response
is to file an issue on the
[Github issue tracker](https://github.com/panzarino/mlbgame/issues/new)

mlbgame's submodules should not really be used other
than as  used by the main functions of the package (in `__init__.py`).

Use of mlbgame must follow the terms stated in the
[license](https://raw.githubusercontent.com/panzarino/mlbgame/master/LICENSE)
and on [mlb.com](http://gd2.mlb.com/components/copyright.txt).

Installation
------------

mlbgame is in the [Python Package Index (PyPI)]
(http://pypi.python.org/pypi/mlbgame/).
Installing with `pip` is recommended for all systems.

mlbgame can be installed by running:

    pip install mlbgame

Alternatively, the latest release of mlbgame can be downloaded as a
[zip](https://github.com/panzarino/mlbgame/archive/master.zip) or
[tarball](https://github.com/panzarino/mlbgame/archive/master.tar.gz).
If you do not install with `pip`, you must also install
`lmxl` as specified in `setup.py`.

If you want to help develop mlbgame,
you must also install the dev dependencies,
which can be done by running `pip install -e .[dev]`
from within the directory.

Examples
--------

Here is a quick teaser to find the scores of all home Mets games for the month
 of June, 2015:

    #!python
    from __future__ import print_function
    import mlbgame

    month = mlbgame.games(2015, 6, home='Mets')
    games = mlbgame.combine_games(month)
    for game in games:
        print(game)

And the output is:

    Giants (5) at Mets (0)
    Giants (8) at Mets (5)
    Giants (4) at Mets (5)
    Braves (3) at Mets (5)
    Braves (5) at Mets (3)
    Braves (8) at Mets (10)
    Blue Jays (3) at Mets (4)
    Blue Jays (2) at Mets (3)
    Reds (1) at Mets (2)
    Reds (1) at Mets (2)
    Reds (1) at Mets (2)
    Reds (2) at Mets (7)
    Cubs (1) at Mets (0)

Maybe you want to know the pitchers for the Royals game on April 30th, 2015:

    #!python
    from __future__ import print_function
    import mlbgame

    day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
    game = day[0]
    output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
    print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))

And the output is:

    Winning pitcher: Y. Ventura (Royals) - Losing Pitcher: C. Wilson (Angels)

You can easily find stats for the Mets batters
in the final game of the 2015 World Series:

    #!python
    from __future__ import print_function
    import mlbgame
    
    game = mlbgame.day(2015, 11, 1, home='Mets')[0]
    stats = mlbgame.player_stats(game.game_id)
    for player in stats.home_batting:
        print(player)

And the output is:

    Curtis Granderson - 1 for 4 with 1 RBI and 1 Home Runs
    David Wright - 1 for 5
    Daniel Murphy - 0 for 3
    Yoenis Cespedes - 0 for 3
    Juan Lagares - 0 for 2
    Lucas Duda - 0 for 2 with 1 RBI
    Travis d'Arnaud - 0 for 5
    Michael Conforto - 2 for 5
    Wilmer Flores - 0 for 4
    Matt Harvey - 0 for 3
    Jeurys Familia - 0 for 0
    Kelly Johnson - 0 for 1
    Jon Niese - 0 for 0
    Addison Reed - 0 for 0
    Bartolo Colon - 0 for 0

"""

import mlbgame.events
import mlbgame.game
import mlbgame.info
import mlbgame.stats
import mlbgame.version

import calendar
from datetime import date, datetime

VERSION = mlbgame.version.__version__
"""Installed version of mlbgame."""


def day(year, month, day, home=None, away=None):
    """Return a list of games for a certain day.

    If the home and away team are the same,
    it will return the game(s) for that team.
    """
    # get the days per month
    daysinmonth = calendar.monthrange(year, month)[1]
    # do not even try to get data if day is too high
    if daysinmonth < day:
        return []
    # get data
    data = mlbgame.game.scoreboard(year, month, day, home=home, away=away)
    return [mlbgame.game.GameScoreboard(data[x]) for x in data]


def games(years, months=None, days=None, home=None, away=None):
    """Return a list of lists of games for multiple days.

    If home and away are the same team, it will return all games for that team.
    """
    # put in data if months and days are not specified
    if months is None:
        months = list(range(1, 13))
    if days is None:
        days = list(range(1, 32))
    results = []
    # check if lists, if not make lists
    # allows users to input either numbers or lists
    if not isinstance(years, list):
        years = [years]
    if not isinstance(months, list):
        months = [months]
    if not isinstance(days, list):
        days = [days]
    for i in years:
        for y in months:
            # get the days in a month
            daysinmonth = calendar.monthrange(i, y)[1]
            for x in days:
                if daysinmonth >= x:
                    # use the day function to get data for each day in range
                    game = day(i, y, x, home=home, away=away)
                    if game:
                        results.append(game)
    return results


def box_score(game_id):
    """Return box score for game matching the game id."""
    # get box score data
    data = mlbgame.game.box_score(game_id)
    # create object with data
    obj = mlbgame.game.GameBoxScore(data)
    return obj


def overview(game_id):
    """Return Overview object that contains game information."""
    return mlbgame.game.Overview(mlbgame.game.overview(game_id))


def players(game_id):
    """Return list players/coaches/umpires for game matching the game id."""
    return mlbgame.game.Players(mlbgame.game.players(game_id))


def combine_games(games):
    """Combines games from multiple days into a single list."""
    return [y for x in games for y in x]


def player_stats(game_id):
    """Return dictionary of player stats for game matching the game id."""
    # get information for that game
    data = mlbgame.stats.player_stats(game_id)
    return mlbgame.stats.Stats(data, game_id, True)


def team_stats(game_id):
    """Return dictionary of team stats for game matching the game id."""
    # get data
    data = mlbgame.stats.team_stats(game_id)
    return mlbgame.stats.Stats(data, game_id, False)


def game_events(game_id):
    """Return dictionary of game events for game matching the game id."""
    data = mlbgame.events.game_events(game_id)
    return [mlbgame.events.Inning(data[x], x) for x in data]


def league():
    """Return Info object that contains league information"""
    return mlbgame.info.Info(mlbgame.info.league_info())


def teams():
    """Return list of Info objects for each team"""
    return [mlbgame.info.Info(x) for x in mlbgame.info.team_info()]


def roster(team_id):
    """Return Roster object that contains roster info for a team"""
    data = mlbgame.info.roster(team_id)
    return mlbgame.info.Roster(data)


def standings(date=datetime.now()):
    """Return Standings object that contains standings info

    date should be a datetime object,
    leave empty to get current standings
    """
    data = mlbgame.info.standings(date)
    return mlbgame.info.Standings(data)


def injury():
    """Return Injuries object that contains injury info"""
    data = mlbgame.info.injury()
    return mlbgame.info.Injuries(data)
