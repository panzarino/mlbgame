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

`mlbgame documentation <http://zachpanz88.github.io/mlbgame>`__

mlbgame on `Github <https://github.com/zachpanz88/mlbgame>`__

Installation
------------

mlbgame is in the `Python Package Index (PyPI) <http://pypi.python.org/pypi/mlbgame/>`__
Installing with ``pip`` is recommended for all systems.

mlbgame can be installed by running:

::

    pip install mlbgame

(You may need to use ``pip2`` if Python 3 is the default on your system.)

mlbgame depends on ``urllib2`` to fetch data from mlb.com.
``urllib2`` will be automatically installed if mlbgame is installed with ``pip``

mlbgame does not yet work on Python 3, but it should work with Python 2.6 and 2.7.

Updating the Game Database
--------------------------

Since games happen every day, new game data exists that is not stored on disk from the original install.
The database can be updated by running the following command:

::

    mlbgame-update-games