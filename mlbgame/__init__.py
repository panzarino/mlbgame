'''
mlbgame is an API to read MLB GameDay XML and JSON data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame currently comes pre-loaded with every game
from 2009 to the end of the 2015 season,
but will be updated regularly during the season.
Therefore, accessing this data does not actually make a request to mlb.com

If you try to get data from a game that is not cached,
mlbgame will download the data from mlb.com.
If the information you request is from completed games,
that data will be cached to disk.
'''

import sys

if sys.version_info[0] != 2:
	print("mlbgame requires Python 2.6+ and does not work with Python 3")
	print("You are running Python version {}.{}".format(sys.version_info.major, sys.version_info.minor))
	sys.exit(1)

import mlbgame.game

from mlbgame import version
VERSION = version.__version__

def one(year, month, day):
	'''
	Return an array of games for a certain day
	'''
	data = mlbgame.game.scoreboard(year, month, day)
	results = []
	for x in data:
		obj = mlbgame.game.Game(data[x])
		results.append(obj)
	return results

def games(year, month, days):
	'''
	Return an array of arrays of games for multiple days
	'''
	results = []
	for x in days:
		game = one(year, month, x)
		results.append(game)
	return results