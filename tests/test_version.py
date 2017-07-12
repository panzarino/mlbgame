#!/usr/bin/env python

import unittest
import mlbgame.version

class TestVersion(unittest.TestCase):
    def test_version(self):
        version = mlbgame.version.__version__
        self.assertIsInstance(version, str)
