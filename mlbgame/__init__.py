'''
mlbgame
-------

mlbgame is an API to read MLB GameDay XML data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame currently comes pre-loaded with scoreboard information for every game
from 2012 to the end of the 2015 season,
but will be updated regularly during the season.
Therefore, accessing this data does not actually make a request to mlb.com.

There is a lot of data for individual games that does not come
pre-installed with mlbgame, but you can install it by running update scripts
shown below. This data is not included becuase it takes up too much space, 
and therefore a request to mlb.com every time is a better option in most cases.

mlbgame [documentation](http://zachpanz88.github.io/mlbgame)

mlbgame on [Github](https://github.com/zachpanz88/mlbgame) (Source Code)

If you have a question or need help, the quickest way to get a response 
is to file an issue on the [Github issue tracker](https://github.com/zachpanz88/mlbgame/issues/new)

mlbgame's submodules (except for `statmap`) should not really be used other than as 
used by the main functions of the package (in `__init__.py`).

Installation
------------

mlbgame is in the [Python Package Index (PyPI)](http://pypi.python.org/pypi/mlbgame/).
Installing with `pip` is recommended for all systems.

mlbgame can be installed by running:

    pip install mlbgame

(You may need to use `pip2` if Python 3 is the default on your system.)

mlbgame does not yet work on Python 3, because it is desinged for Python 2.6 and 2.7.

Updating the Game Database
--------------------------

Since games happen every day, new game data exists that is not stored on disk from the original install.
The database can be updated by running the following command:

    mlbgame-update-games

There are some optional arguments that will cache extra data that is not included with the original install.
This extra data may take up a lot of disk space, so only cache if you really need it (it will make processes much faster).
If this data is not cached, mlbgame will make a request to mlb.com every time you try to access the data.

    usage: mlbgame-update-games <arguments>
    
    Arguments:
    -h (--help)\t\t\tdisplay this help menu
    --hide\t\t\thides output from update script
    --extra\t\t\tsaves the box scores and individual game stats from every game
    --start_date <year>\t\tyear to start updating from (runs until current day)

Examples
--------

Here is a quick teaser to find the scores of all home Mets games for the month of June, 2015:

    #!python
    import mlbgame
    
    month = mlbgame.games(2015, 6, home="Mets")
    games = mlbgame.combine_games(month)
    for x in games:
        print x
    
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
    import mlbgame
    
    day = mlbgame.day(2015, 4, 12, home="Royals", away="Royals")
    game = day[0]
    output = "Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)"
    print output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team)

And the output is:

    Winning pitcher: Y. Ventura (Royals) - Losing Pitcher: C. Wilson (Angels)

Finding stats for the Mets batters
in the final game of the 2015 World Series
can also be done:

    import mlbgame
    
    game = mlbgame.day(2015, 11, 1, home="Mets")[0]
    stats = mlbgame.player_stats(game.game_id)
    for x in stats['home_batting']:
        print x

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

Use of mlbgame implies agreement to the terms stated in the 
[license](https://raw.githubusercontent.com/zachpanz88/mlbgame/master/LICENSE) 
and on [mlb.com](http://gd2.mlb.com/components/copyright.txt)

'''

import sys

if sys.version_info[0] != 2 or sys.version_info[1] < 6:
	print("mlbgame is designed for Python 2.6+ and does not work with Python 3")
	print("You are running Python version {}.{}".format(sys.version_info.major, sys.version_info.minor))
	sys.exit(1)

import mlbgame.game
import mlbgame.stats
import calendar
from datetime import date

import mlbgame.version
VERSION = mlbgame.version.__version__
'''
Installed version of mlbgame
'''

def day(year, month, day, home=None, away=None):
	'''
	Return a list of games for a certain day
	
	If the home and away team are the same, it will return the game(s) for that team
	'''
	daysinmonth = calendar.monthrange(year, month)[1]
	if daysinmonth < day:
		return []
	today = date.today()
	if year > today.year:
		return []
	elif year >= today.year and month > today.month:
		return []
	elif year >= today.year and month >= today.month and day > today.day:
		return []
	data = mlbgame.game.scoreboard(year, month, day, home=home, away=away)
	results = []
	for x in data:
		obj = mlbgame.game.GameScoreboard(data[x])
		results.append(obj)
	return results

def games(years, months=None, days=None, home=None, away=None):
	'''
	Return a list of lists of games for multiple days
	
	If home and away are the same team, it will return all games for that team
	'''
	if months == None:
		months = []
		for x in range(1, 13):
			months.append(x)
	if days == None:
		days = []
		for x in range(1, 32):
			days.append(x)
	results = []
	if not isinstance(years, list):
		years = [years]
	if not isinstance(months, list):
		months = [months]
	if not isinstance(days, list):
		days = [days]
	for i in years:
		for y in months:
			daysinmonth = calendar.monthrange(i, y)[1]
			for x in days:
				if daysinmonth >= x:
					game = day(i, y, x, home=home, away=away)
					if game != []:
						results.append(game)
	return results

def box_score(game_id):
	'''
	Return box score for game matching the game id
	'''
	data = mlbgame.game.box_score(game_id)
	obj = mlbgame.game.GameBoxScore(data)
	return obj

def combine_games(games):
	'''
	Combines games from multiple days into a single list
	'''
	output = []
	for x in games:
		for y in x:
			output.append(y)
	return output

def player_stats(game_id):
	'''
	Return dictionary of player stats for game matching the game id
	'''
	data = mlbgame.stats.get_stats(game_id)
	output = {'home_pitching': [], 'away_pitching': [], 'home_batting': [], 'away_batting': []}
	for y in data:
		for x in data[y]:
			if y == 'home_pitching' or y == 'away_pitching':
				obj = mlbgame.stats.PitcherStats(x)
			elif y == 'home_batting' or y == 'away_batting':
				obj = mlbgame.stats.BatterStats(x)
			output[y].append(obj)
	return output

def combine_stats(stats):
	'''
	Combines player stat objects from a game into a single list
	'''
	output = []
	for x in stats:
		for y in stats[x]:
			output.append(y)
	return output