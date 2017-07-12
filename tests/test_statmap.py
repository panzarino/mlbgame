#!/usr/bin/env python

import unittest

class TestStatmap(unittest.TestCase):

    def test_statmap(self):
        import mlbgame.statmap
        statmap = mlbgame.statmap.idmap
        self.assertIsInstance(statmap, dict)
