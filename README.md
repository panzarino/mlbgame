# mlbgame

[![Build Status](https://travis-ci.org/panzarino/mlbgame.svg)](https://travis-ci.org/panzarino/mlbgame)
[![Code Climate](https://codeclimate.com/github/panzarino/mlbgame/badges/gpa.svg)](https://codeclimate.com/github/panzarino/mlbgame)
[![Coverage Status](https://coveralls.io/repos/github/panzarino/mlbgame/badge.svg?branch=master)](https://coveralls.io/github/panzarino/mlbgame?branch=master)


[![Join Slack](https://img.shields.io/badge/slack-join-blue.svg)](https://mlbgame-slack-invite.herokuapp.com/)

mlbgame is a Python API to retrieve and read MLB GameDay data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame [documentation](http://panz.io/mlbgame)

mlbgame on [Github](https://github.com/panzarino/mlbgame) (Source Code)

If you have a question or need help, the quickest way to get a response 
is to file an issue on the [Github issue tracker](https://github.com/panzarino/mlbgame/issues/new)

mlbgame's submodules should not really be used other than as 
used by the main functions of the package (in `__init__.py`).

Use of mlbgame must follow the terms stated in the 
[license](https://raw.githubusercontent.com/panzarino/mlbgame/master/LICENSE) 
and on [mlb.com](http://gd2.mlb.com/components/copyright.txt).

Installation
------------

mlbgame is in the [Python Package Index (PyPI)](http://pypi.python.org/pypi/mlbgame/).
Installing with `pip` is recommended for all systems.

mlbgame can be installed by running:

    pip install mlbgame

Alternatively, the latest release of mlbgame can be downloaded as a 
[zip](https://github.com/panzarino/mlbgame/archive/master.zip) or [tarball](https://github.com/panzarino/mlbgame/archive/master.tar.gz). 
If you do not install with `pip`, you must also install `lxml` as specified in `setup.py`.

If you want to help develop mlbgame, you must also install the dev dependencies, which can be done by running `pip install -e .[dev]` from within the directory.

Examples
--------

Here is a quick teaser to find the scores of all home Mets games for the month of June, 2015:

```python
from __future__ import print_function
import mlbgame

month = mlbgame.games(2015, 6, home='Mets')
games = mlbgame.combine_games(month)
for game in games:
    print(game)
```

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

```python
from __future__ import print_function
import mlbgame

day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
game = day[0]
output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))
```

And the output is:

    Winning pitcher: Y. Ventura (Royals) - Losing Pitcher: C. Wilson (Angels)

You can easily find stats for the Mets batters
in the final game of the 2015 World Series:

```python
from __future__ import print_function
import mlbgame

game = mlbgame.day(2015, 11, 1, home='Mets')[0]
stats = mlbgame.player_stats(game.game_id)
for player in stats.home_batting:
    print(player)
```

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
    
