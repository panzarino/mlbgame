#!/usr/bin/env python

import unittest

import mlbgame

from datetime import datetime


class TestGame(unittest.TestCase):

    def test_day(self):
        games = mlbgame.day(2016, 8, 2)
        for game in games:
            if game.home_team == 'Mets':
                g = game
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
            self.assertIsInstance(game.nice_score(), str)
        game = g
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
        self.assertEqual(game.__str__(), 'Yankees (1) at Mets (7)')

    def test_games(self):
        games = mlbgame.games(2016, 7)
        self.assertIsInstance(games, list)
        for day in games:
            self.assertIsInstance(day, list)
            for game in day:
                self.assertIsInstance(game, mlbgame.game.GameScoreboard)
        games = mlbgame.combine_games(games)
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
            self.assertIsInstance(game.nice_score(), str)
            if game.game_tag == 'go_game':
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

    def test_box_score(self):
        box_score = mlbgame.box_score('2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(box_score.game_id, '2016_08_02_nyamlb_nynmlb_1')
        self.assertIsInstance(box_score.innings, list)
        for inning in box_score:
            self.assertIn('inning', inning)
            self.assertIn('away', inning)
            self.assertIn('home', inning)
        self.assertEqual(box_score.innings[0]['inning'], 1)
        self.assertEqual(box_score.innings[0]['away'], 0)
        self.assertEqual(box_score.innings[0]['home'], 0)
        self.assertEqual(box_score.innings[1]['inning'], 2)
        self.assertEqual(box_score.innings[1]['away'], 0)
        self.assertEqual(box_score.innings[1]['home'], 0)
        self.assertEqual(box_score.innings[2]['inning'], 3)
        self.assertEqual(box_score.innings[2]['away'], 0)
        self.assertEqual(box_score.innings[2]['home'], 2)
        self.assertEqual(box_score.innings[3]['inning'], 4)
        self.assertEqual(box_score.innings[3]['away'], 0)
        self.assertEqual(box_score.innings[3]['home'], 0)
        self.assertEqual(box_score.innings[4]['inning'], 5)
        self.assertEqual(box_score.innings[4]['away'], 0)
        self.assertEqual(box_score.innings[4]['home'], 1)
        self.assertEqual(box_score.innings[5]['inning'], 6)
        self.assertEqual(box_score.innings[5]['away'], 0)
        self.assertEqual(box_score.innings[5]['home'], 0)
        self.assertEqual(box_score.innings[6]['inning'], 7)
        self.assertEqual(box_score.innings[6]['away'], 0)
        self.assertEqual(box_score.innings[6]['home'], 4)
        self.assertEqual(box_score.innings[7]['inning'], 8)
        self.assertEqual(box_score.innings[7]['away'], 0)
        self.assertEqual(box_score.innings[7]['home'], 0)
        self.assertEqual(box_score.innings[8]['inning'], 9)
        self.assertEqual(box_score.innings[8]['away'], 1)
        self.assertEqual(box_score.innings[8]['home'], 'x')
        self.assertEqual(box_score.print_scoreboard(), (
            'Inning\t1 2 3 4 5 6 7 8 9 \n'
            '---------------------------\n'
            'Away\t0 0 0 0 0 0 0 0 1 \n'
            'Home\t0 0 2 0 1 0 4 0 x '
            ))
