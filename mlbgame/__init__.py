import sys

if sys.version_info[0] != 2:
	print("mlbgame requires Python 2.6+ and does not work with Python 3")
	print("You are running Python version {}.{}".format(sys.version_info.major, sys.version_info.minor))
	sys.exit(1)

from mlbgame import version
VERSION = version.__version__

def games(year, month, day):
	import mlbgame.game as game
	data = game.scoreboard(year, month, day)
	results = []
	for x in data:
		obj = game.Game(data[x])
		results.append(obj)
	return results