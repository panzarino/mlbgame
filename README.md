# mlbgame

![mlbgame demo](http://i.imgur.com/h2kYOyd.gif "mlbgame demo")

mlbgame is a Python API to retrieve and read MLB GameDay XML data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame currently comes pre-loaded with scoreboard information for every game
from 2012 to the end of the 2015 season,
but will be updated regularly during the season.
Therefore, accessing this data does not actually make a request to mlb.com.

If you try to get data from a game that is not cached,
mlbgame will download the data from mlb.com.

There are a lot of extra data for individual games that do not come
pre-installed with mlbgame, but can be installed by running update scripts
shown below. This data is not included becuase it takes up too much space, 
and therefore a request to mlb.com every time is a better option 
because not everyone will want to access this data.

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

Alternatively, the latest release of mlbgame can be downloaded as a 
[zip](https://github.com/zachpanz88/mlbgame/archive/master.zip) or [tarball](https://github.com/zachpanz88/mlbgame/archive/master.tar.gz). 
If you do not install with `pip`, you must also install [lxml](http://lxml.de/) for mlbgame to work.

Updating the Game Database
--------------------------

Since games happen every day, new game data exists that is not stored on disk from the original install.
The database can be updated by running the following command:

    mlbgame-update

There are some optional arguments that will cache extra data that is not included with the original install.
This extra data may take up a lot of disk space, so only cache if you really need it (it will make processes much faster).
If this data is not cached, mlbgame will make a request to mlb.com every time you try to access the data.

    usage: mlbgame-update <arguments>
    
    Arguments:
    --help (-h): display this help menu
    --hide: hides output from update script
    --more (-m): saves the box scores and individual game stats from every game
    --start (-s) <MM-DD-YYYY>: date to start updating from (default: 01-01-2012)
    --end (-e) <MM-DD-YYYY>: date to update until (default: current day)

Use of mlbgame must follow the terms stated in the 
[license](https://raw.githubusercontent.com/zachpanz88/mlbgame/master/LICENSE) 
and on [mlb.com](http://gd2.mlb.com/components/copyright.txt>).

Examples
--------

Here is a quick teaser to find the scores of all home Mets games for the month of June, 2015:

```python
from __future__ import print_function
import mlbgame

month = mlbgame.games(2015, 6, home="Mets")
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

day = mlbgame.day(2015, 4, 12, home="Royals", away="Royals")
game = day[0]
output = "Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)"
print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))
```

And the output is:

    Winning pitcher: Y. Ventura (Royals) - Losing Pitcher: C. Wilson (Angels)

You can easily find stats for the Mets batters
in the final game of the 2015 World Series:

```python
from __future__ import print_function
import mlbgame

game = mlbgame.day(2015, 11, 1, home="Mets")[0]
stats = mlbgame.player_stats(game.game_id)
for player in stats['home_batting']:
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
    
