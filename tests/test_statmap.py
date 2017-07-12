#!/usr/bin/env python

import unittest
import mlbgame.statmap

class TestStatmap(unittest.TestCase):
    def test_statmap(self):
        statmap = mlbgame.statmap.idmap
        self.assertIsInstance(statmap, dict)