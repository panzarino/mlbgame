=======
mlbgame
=======

mlbgame is a Python API to retrieve and read MLB GameDay data.
mlbgame works with real time data, getting information as games are being played.

mlbgame uses the same data that MLB GameDay uses,
and therefore is updated as soon as something happens in a game.

mlbgame `documentation <http://panz.io/mlbgame>`__

mlbgame on `Github <https://github.com/panzarino/mlbgame>`__  (Source Code)

If you have a question or need help, the quickest way to get a response 
is to file an issue on the `Github issue tracker <https://github.com/panzarino/mlbgame/issues/new>`__

mlbgame's submodules should not really be used other than as 
used by the main functions of the package (in ``__init__.py``).

Use of mlbgame must follow the terms stated in the 
`license <https://raw.githubusercontent.com/panzarino/mlbgame/master/LICENSE>`__ 
and on `mlb.com <http://gd2.mlb.com/components/copyright.txt>`__

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
If you do not install with ``pip``, you must also install ``lmxl`` as specified in ``setup.py``.

If you want to help develop mlbgame, you must also install the dev dependencies, which can be done by running ``pip install -e .[dev]`` from within the directory.
