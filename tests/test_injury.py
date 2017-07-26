#!/usr/bin/env python

import unittest


class TestInjury(unittest.TestCase):
    
    def test_injury(self):
        import mlbgame
        injury = mlbgame.injury(121)
        self.assertIsInstance(injury.injuries, list)
        for player in injury.injuries:
            self.assertIsInstance(player.display_ts, str)
            self.assertIsInstance(player.due_back, str)
            self.assertIsInstance(player.injury_desc, str)
            self.assertIsInstance(player.injury_status, str)
            self.assertIsInstance(player.injury_update, str)
            self.assertIsInstance(player.insert_ts, str)
            self.assertIsInstance(player.league_id, int)
            self.assertIsInstance(player.name_first, str)
            self.assertIsInstance(player.name_last, str)
            self.assertIsInstance(player.player_id, int)
            self.assertIsInstance(player.position, str)
            self.assertIsInstance(player.team_id, int)
            self.assertIsInstance(player.team_name, str)
            self.assertEqual(player.team_id, 121)
            self.assertEqual(player.team_name, 'Mets')
