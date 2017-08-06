#!/usr/bin/env python

import unittest


class TestGame(unittest.TestCase):

    def test_day(self):
        import mlbgame
        from datetime import datetime
        games = mlbgame.day(2016, 8, 2)
        for game in games:
            self.assertIsInstance(game.away_team, str)
            self.assertIsInstance(game.away_team_errors, int)
            self.assertIsInstance(game.away_team_hits, int)
            self.assertIsInstance(game.away_team_runs, int)
            self.assertIsInstance(game.date, datetime)
            self.assertIsInstance(game.game_id, str)
            self.assertIsInstance(game.game_league, str)
            self.assertIsInstance(game.game_start_time, str)
            self.assertIsInstance(game.game_status, str)
            self.assertIsInstance(game.game_tag, str)
            self.assertIsInstance(game.home_team, str)
            self.assertIsInstance(game.home_team_errors, int)
            self.assertIsInstance(game.home_team_hits, int)
            self.assertIsInstance(game.home_team_runs, int)
            self.assertIsInstance(game.l_pitcher, str)
            self.assertIsInstance(game.l_pitcher_losses, int)
            self.assertIsInstance(game.l_pitcher_wins, int)
            self.assertIsInstance(game.l_team, str)
            self.assertIsInstance(game.sv_pitcher, str)
            self.assertIsInstance(game.sv_pitcher_saves, int)
            self.assertIsInstance(game.w_pitcher, str)
            self.assertIsInstance(game.w_pitcher_losses, int)
            self.assertIsInstance(game.w_pitcher_wins, int)
            self.assertIsInstance(game.w_team, str)
        game = games[0]
        self.assertEqual(game.away_team, 'Yankees')
        self.assertEqual(game.away_team_errors, 2)
        self.assertEqual(game.away_team_hits, 6)
        self.assertEqual(game.away_team_runs, 1)
        self.assertEqual(game.date, datetime(2016, 8, 2, 18, 10))
        self.assertEqual(game.game_id, '2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(game.game_league, 'AN')
        self.assertEqual(game.game_start_time, '7:10PM')
        self.assertEqual(game.game_status, 'FINAL')
        self.assertEqual(game.game_tag, 'go_game')
        self.assertEqual(game.home_team, 'Mets')
        self.assertEqual(game.home_team_errors, 0)
        self.assertEqual(game.home_team_hits, 10)
        self.assertEqual(game.home_team_runs, 7)
        self.assertEqual(game.l_pitcher, 'M. Tanaka')
        self.assertEqual(game.l_pitcher_losses, 4)
        self.assertEqual(game.l_pitcher_wins, 7)
        self.assertEqual(game.l_team, 'Yankees')
        self.assertEqual(game.sv_pitcher, '. ')
        self.assertEqual(game.sv_pitcher_saves, 0)
        self.assertEqual(game.w_pitcher, 'J. deGrom')
        self.assertEqual(game.w_pitcher_losses, 5)
        self.assertEqual(game.w_pitcher_wins, 7)
        self.assertEqual(game.w_team, 'Mets')
