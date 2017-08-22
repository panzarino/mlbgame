#!/usr/bin/env python

import unittest

import mlbgame


class TestStats(unittest.TestCase):

    def __test_team_picher_stats(self, team):
        self.assertIsInstance(team.bb, int)
        self.assertIsInstance(team.bf, int)
        self.assertIsInstance(team.er, int)
        self.assertIsInstance(team.era, float)
        self.assertIsInstance(team.h, int)
        self.assertIsInstance(team.hr, int)
        self.assertIsInstance(team.out, int)
        self.assertIsInstance(team.r, int)
        self.assertIsInstance(team.so, int)
        self.assertIsInstance(team.team_flag, str)

    def __test_team_batter_stats(self, team):
        self.assertIsInstance(team.ab, int)
        self.assertIsInstance(team.avg, float)
        self.assertIsInstance(team.bb, int)
        self.assertIsInstance(team.d, int)
        self.assertIsInstance(team.da, int)
        self.assertIsInstance(team.h, int)
        self.assertIsInstance(team.hr, int)
        self.assertIsInstance(team.lob, int)
        self.assertIsInstance(team.obp, float)
        self.assertIsInstance(team.ops, float)
        self.assertIsInstance(team.po, int)
        self.assertIsInstance(team.r, int)
        self.assertIsInstance(team.rbi, int)
        self.assertIsInstance(team.slg, float)
        self.assertIsInstance(team.so, int)
        self.assertIsInstance(team.t, int)
        self.assertIsInstance(team.team_flag, str)

    def test_team_stats(self):
        stats = mlbgame.team_stats('2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(stats.game_id, '2016_08_02_nyamlb_nynmlb_1')
        self.__test_team_picher_stats(stats.away_pitching)
        self.__test_team_picher_stats(stats.home_pitching)
        self.__test_team_batter_stats(stats.away_batting)
        self.__test_team_batter_stats(stats.home_batting)
        pitching = stats.home_pitching
        batting = stats.home_batting
        self.assertEqual(pitching.bb, 2)
        self.assertEqual(pitching.bf, 35)
        self.assertEqual(pitching.er, 1)
        self.assertEqual(pitching.era, 3.35)
        self.assertEqual(pitching.h, 6)
        self.assertEqual(pitching.hr, 1)
        self.assertEqual(pitching.out, 27)
        self.assertEqual(pitching.r, 1)
        self.assertEqual(pitching.so, 10)
        self.assertEqual(pitching.team_flag, 'home')
        self.assertEqual(batting.ab, 35)
        self.assertEqual(batting.avg, 0.238)
        self.assertEqual(batting.bb, 0)
        self.assertEqual(batting.d, 3)
        self.assertEqual(batting.da, 7)
        self.assertEqual(batting.h, 10)
        self.assertEqual(batting.hr, 2)
        self.assertEqual(batting.lob, 10)
        self.assertEqual(batting.obp, 0.309)
        self.assertEqual(batting.ops, 0.717)
        self.assertEqual(batting.po, 27)
        self.assertEqual(batting.r, 7)
        self.assertEqual(batting.rbi, 7)
        self.assertEqual(batting.slg, 0.408)
        self.assertEqual(batting.so, 5)
        self.assertEqual(batting.t, 0)
        self.assertEqual(batting.team_flag, 'home')
