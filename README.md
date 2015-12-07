# mlbgame

mlbgame is an API to read MLB GameDay XML and JSON data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame currently comes pre-loaded with every game
from 2012 to the end of the 2015 season,
but will be updated regularly during the season.
Therefore, accessing this data does not actually make a request to mlb.com.

If you try to get data from a game that is not cached,
mlbgame will download the data from mlb.com.

mlbgame [documentation](http://zachpanz88.github.io/mlbgame)

mlbgame on [Github](https://github.com/zachpanz88/mlbgame) (Source Code) (Leave a star!)

Installation
------------

mlbgame is in the [Python Package Index (PyPI)](http://pypi.python.org/pypi/mlbgame/).
Installing with `pip` is recommended for all systems.

mlbgame can be installed by running:

```
pip install mlbgame
```

(You may need to use `pip2` if Python 3 is the default on your system.)

mlbgame does not yet work on Python 3, but it should work with Python 2.6 and 2.7.

Updating the Game Database
--------------------------

Since games happen every day, new game data exists that is not stored on disk from the original install.
The database can be updated by running the following command:

```
mlbgame-update-games
```

There are some optional arguments that will cache extra data that is not included with the original install.
This extra data may take up a lot of disk space, so only cache if you really need it (it will make processes much faster).
If this data is not cached, mlbgame will make a request to mlb.com every time you try to access the data.

```
usage: mlbgame-update-games <arguments>
    
Arguments:
-h (--help)             display this help menu
--hide                  hides output from update script
--box_score             caches the box scores and individual game stats from every game
--start_date <year>     year to start updating from (runs until current day)
```


Examples
--------

Here is a quick teaser to find the scores of all home Mets games for the month of June, 2015:

```python
import mlbgame
    
month = mlbgame.games(2015, 6, home="Mets")
games = mlbgame.combine_games(month)
for x in games:
    print x
```

And the output is:

```
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
```

Or you could find the scores of every game on July 4th, 2015:

```python
import mlbgame

day = mlbgame.day(2015, 7, 4)
for game in day:
    print game
```

And the output is:

```
Angels (13) at Rangers (0)
Indians (0) at Pirates (1)
Rockies (3) at D-backs (7)
Rays (2) at Yankees (3)
Mets (3) at Dodgers (4)
Orioles (2) at White Sox (3)
Phillies (5) at Braves (9)
Mariners (0) at Athletics (2)
Giants (3) at Nationals (9)
Brewers (7) at Reds (3)
Padres (1) at Cardinals (2)
Twins (5) at Royals (3)
Astros (1) at Red Sox (6)
Marlins (2) at Cubs (7)
Blue Jays (3) at Tigers (8)
```

Maybe you want to know the pitchers for the Royals game on April 30th, 2015:

```python
import mlbgame
    
day = mlbgame.day(2015, 4, 12, home="Royals", away="Royals")
game = day[0]
output = "Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)"
print output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team)
```

And the output is:

```
Winning pitcher: Y. Ventura (Royals) - Losing Pitcher: C. Wilson (Angels)
```

Finding stats for the Mets batters
in the final game of the 2015 World Series
can also be done:

```python
import mlbgame
    
game = mlbgame.day(2015, 11, 1, home="Mets")[0]
stats = mlbgame.stats(game.game_id)
for x in stats['home_batting']:
    print x
```

And the output is:

```
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
```

Use of mlbgame must follow the terms stated in the 
[license](https://raw.githubusercontent.com/zachpanz88/mlbgame/master/LICENSE) 
and on [mlb.com](http://gd2.mlb.com/components/copyright.txt)
