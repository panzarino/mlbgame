=======
mlbgame
=======

mlbgame is a Python API to retrieve and read MLB GameDay XML data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame currently comes pre-loaded with scoreboard information for every game
from 2012 to the end of the 2016 season. 
Therefore, accessing this data does not actually make a request to mlb.com.

If you try to get data from a game that is not cached,
mlbgame will download the data from mlb.com.

There are a lot of extra data for individual games that do not come
pre-installed with mlbgame, but can be installed by running update scripts
shown below. This data is not included because it takes up too much space, 
and therefore a request to mlb.com every time is a better option 
because not everyone will want to access this data.

mlbgame `documentation <http://panz.io/mlbgame>`__

mlbgame on `Github <https://github.com/panzarino/mlbgame>`__  (Source Code)

If you have a question or need help, the quickest way to get a response 
is to file an issue on the `Github issue tracker <https://github.com/panzarino/mlbgame/issues/new>`__

mlbgame's submodules (except for ``statmap``) should not really be used other than as 
used by the main functions of the package (in ``__init__.py``).

Installation
------------

mlbgame is in the `Python Package Index (PyPI) <http://pypi.python.org/pypi/mlbgame/>`__.
Installing with ``pip`` is recommended for all systems.

mlbgame can be installed by running:

::

    pip install mlbgame

Alternatively, the latest release of mlbgame can be downloaded as a 
`zip <https://github.com/panzarino/mlbgame/archive/master.zip>`__ or 
`tarball <https://github.com/panzarino/mlbgame/archive/master.tar.gz>`__.
If you do not install with ``pip``, you must also install `lxml <http://lxml.de/>`__ for mlbgame to work.

Updating the Game Database
--------------------------

Since games happen every day, new game data exists that is not stored on disk from the original install.
The database can be updated by running the following command:

::

    mlbgame-update

There are some optional arguments that will cache extra data that is not included with the original install.
This extra data may take up a lot of disk space, so only cache if you really need it (it will make processes much faster).
If this data is not cached, mlbgame will make a request to mlb.com every time you try to access the data.

::

    usage: mlbgame-update <arguments>
    
    Arguments:
    --help (-h): display this help menu
    --clear: delete all cached data
    --hide: hides output from update script
    --stats: saves the box scores and individual game stats from every game
    --events: saves the game events from every game
    --overview: saves the game overview from every game
    --start (-s) <MM-DD-YYYY>: date to start updating from (default: 01-01-2012)
    --end (-e) <MM-DD-YYYY>: date to update until (default: current day)

Use of mlbgame must follow the terms stated in the 
`license <https://raw.githubusercontent.com/panzarino/mlbgame/master/LICENSE>`__ 
and on `mlb.com <http://gd2.mlb.com/components/copyright.txt>`__
