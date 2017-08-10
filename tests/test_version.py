#!/usr/bin/env python

import unittest

import mlbgame


class TestVersion(unittest.TestCase):

    def test_version_module(self):
        version = mlbgame.version.__version__
        self.assertIsInstance(version, str)

    def test_version_variable(self):
        version = mlbgame.VERSION
        self.assertIsInstance(version, str)
