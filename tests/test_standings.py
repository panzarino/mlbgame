#!/usr/bin/env python

import unittest


class TestStandings(unittest.TestCase):
    
    def test_standings(self):
        import mlbgame
        from datetime import datetime
        standings = mlbgame.standings()
        self.assertEquals(standings.standings_schedule_date, 'standings_schedule_date')
        self.assertIsInstance(standings.last_update, datetime)
        self.assertIsInstance(standings.divisions, list)
        for division in standings.divisions:
            self.assertIsInstance(division.name, str)
            self.assertIsInstance(division.teams, list)
            for team in division.teams:
                self.assertIsInstance(team.away, str)
                self.assertIsInstance(team.clinched_sw, str)
                self.assertIsInstance(team.division, str)
                self.assertIsInstance(team.division_champ, str)
                self.assertIsInstance(team.division_id, int)
                self.assertIsInstance(team.division_odds, float)
                self.assertIsInstance(team.elim, (str, int))
                self.assertIsInstance(team.elim_wildcard, (str, int))
                self.assertIsInstance(team.extra_inn, str)
                self.assertIsInstance(team.file_code, str)
                self.assertIsInstance(team.gb, (str, float))
                self.assertIsInstance(team.gb_wildcard, (str, float))
                self.assertIsInstance(team.home, str)
                self.assertIsInstance(team.interleague, str)
                self.assertIsInstance(team.is_wildcard_sw, str)
                self.assertIsInstance(team.l, int)
                self.assertIsInstance(team.last_ten, str)
                self.assertIsInstance(team.one_run, str)
                self.assertIsInstance(team.opp_runs, int)
                self.assertIsInstance(team.pct, float)
                self.assertIsInstance(team.place, int)
                self.assertIsInstance(team.playoff_odds, float)
                self.assertIsInstance(team.playoff_points_sw, str)
                self.assertIsInstance(team.playoffs_flag_milb, str)
                self.assertIsInstance(team.playoffs_flag_mlb, str)
                self.assertIsInstance(team.playoffs_sw, str)
                self.assertIsInstance(team.points, str)
                self.assertIsInstance(team.runs, int)
                self.assertIsInstance(team.sit_code, str)
                self.assertIsInstance(team.streak, str)
                self.assertIsInstance(team.team_abbrev, str)
                self.assertIsInstance(team.team_full, str)
                self.assertIsInstance(team.team_id, int)
                self.assertIsInstance(team.team_short, str)
                self.assertIsInstance(team.vs_central, str)
                self.assertIsInstance(team.vs_division, str)
                self.assertIsInstance(team.vs_east, str)
                self.assertIsInstance(team.vs_left, str)
                self.assertIsInstance(team.vs_right, str)
                self.assertIsInstance(team.vs_west, str)
                self.assertIsInstance(team.w, int)
                self.assertIsInstance(team.wild_card, str)
                self.assertIsInstance(team.wildcard_odds, float)
                self.assertIsInstance(team.x_wl, str)
                self.assertIsInstance(team.x_wl_seas, str)

    def test_standings_historical(self):
        pass
