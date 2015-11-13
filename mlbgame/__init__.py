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