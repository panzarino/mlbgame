#!/usr/bin/env python

import unittest

class TestVersion(unittest.TestCase):

    def test_version_module(self):
        import mlbgame.version
        version = mlbgame.version.__version__
        self.assertIsInstance(version, str)

    def test_version_variable(self):
        import mlbgame
        version = mlbgame.VERSION
        self.assertIsInstance(version, str)
