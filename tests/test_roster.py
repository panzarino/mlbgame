#!/usr/bin/env python

import unittest


class TestRoster(unittest.TestCase):

    def test_roster(self):
        import mlbgame
        roster = mlbgame.roster(121)
        self.assertIsInstance(roster.roster, list)
        for player in roster.roster:
            self.assertIsInstance(player.bats, str)
            self.assertIsInstance(player.birth_date, str)
            self.assertIsInstance(player.college, str)
            self.assertIsInstance(player.end_date, str)
            self.assertIsInstance(player.height_feet, int)
            self.assertIsInstance(player.height_inches, int)
            self.assertIsInstance(player.jersey_number, int)
            self.assertIsInstance(player.name_display_first_last, str)
            self.assertIsInstance(player.name_display_last_first, str)
            self.assertIsInstance(player.name_first, str)
            self.assertIsInstance(player.name_full, str)
            self.assertIsInstance(player.name_last, str)
            self.assertIsInstance(player.name_use, str)
            self.assertIsInstance(player.player_id, int)
            self.assertIsInstance(player.position_txt, str)
            self.assertIsInstance(player.primary_position, int)
            self.assertIsInstance(player.pro_debut_date, str)
            self.assertIsInstance(player.start_date, str)
            self.assertIsInstance(player.starter_sw, str)
            self.assertIsInstance(player.status_code, str)
            self.assertIsInstance(player.team_abbrev, str)
            self.assertIsInstance(player.team_code, str)
            self.assertIsInstance(player.team_id, int)
            self.assertIsInstance(player.team_name, str)
            self.assertIsInstance(player.throws, str)
            self.assertIsInstance(player.weight, int)
            self.assertEqual(player.team_abbrev, 'NYM')
            self.assertEqual(player.team_code, 'nyn')
            self.assertEqual(player.team_id, 121)
            self.assertEqual(player.team_name, 'New York Mets')
