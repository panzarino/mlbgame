#!/usr/bin/env python

import unittest

import mlbgame
from mlbgame.events import (Action, AtBat)


class TestEvents(unittest.TestCase):

    def test_game_events(self):
        """Test that game events properties are of the correct type and that
        the first atbat event and first action event of the match
            http://gd2.mlb.com/components/game/mlb/year_2016/month_08/day_02/gid_2016_08_02_nyamlb_nynmlb_1/game_events.xml
        are exactly correct."""
        events = mlbgame.game_events('2016_08_02_nyamlb_nynmlb_1')
        for inning in events:
            self.assertIsInstance(inning.num, int)
            self.assertIsInstance(inning.top, list)
            self.assertIsInstance(inning.bottom, list)
            atbats_actions = inning.top + inning.bottom
            for atbat_action in atbats_actions:
                if isinstance(atbat_action, AtBat) and atbat_action.num == 1:
                    # test an atbat
                    self.assertEqual(inning.num, 1)
                    self.assertEqual(inning.__str__(), 'Inning 1')
                    self.assertEqual(atbat_action.away_team_runs, 0)
                    self.assertEqual(atbat_action.b, 1)
                    self.assertEqual(atbat_action.b1, '')
                    self.assertEqual(atbat_action.b2, '')
                    self.assertEqual(atbat_action.b3, '')
                    self.assertEqual(atbat_action.batter, 458731)
                    self.assertEqual(atbat_action.des, 'Brett Gardner flies out to center fielder Alejandro De Aza.  ')
                    self.assertEqual(atbat_action.des_es, 'Brett Gardner batea elevado de out a jardinero central Alejandro De Aza.  ')
                    self.assertEqual(atbat_action.event, 'Flyout')
                    self.assertEqual(atbat_action.event_es, 'Elevado de Out')
                    self.assertEqual(atbat_action.event_num, 6)
                    self.assertEqual(atbat_action.home_team_runs, 0)
                    self.assertEqual(atbat_action.num, 1)
                    self.assertEqual(atbat_action.o, 1)
                    self.assertEqual(atbat_action.pitcher, 594798)
                    self.assertEqual(atbat_action.play_guid, 'e91fe0bf-6e1e-40a3-953c-47a943b37638')
                    self.assertEqual(atbat_action.s, 0)
                    self.assertEqual(atbat_action.start_tfs, 231105)
                    self.assertEqual(atbat_action.start_tfs_zulu, '2016-08-02T23:11:05Z')
                    self.assertEqual(atbat_action.__str__(), 'Brett Gardner flies out to center fielder Alejandro De Aza.  ')
                    pitch = atbat_action.pitches[0]
                    self.assertEqual(pitch.des, 'Ball')
                    self.assertEqual(pitch.des_es, 'Bola mala')
                    self.assertEqual(pitch.pitch_type, 'FT')
                    self.assertEqual(pitch.start_speed, 95.2)
                    self.assertEqual(pitch.type, 'B')
                    self.assertEqual(pitch.__str__(), 'Pitch: FT at 95.2: Ball')
                if atbat_action.event_num == 229 and isinstance(atbat_action, Action):
                    # test an action
                    self.assertEqual(inning.num, 4)
                    self.assertEqual(inning.__str__(), 'Inning 4')
                    self.assertEqual(atbat_action.away_team_runs, 0)
                    self.assertEqual(atbat_action.b, 1)
                    self.assertEqual(atbat_action.des, 'With Michael Conforto batting, wild pitch by Masahiro Tanaka, James Loney to 2nd.  ')
                    self.assertEqual(atbat_action.des_es, 'Con Michael Conforto bateando, lanzamiento desviado de Masahiro Tanaka, James Loney a 2da.  ')
                    self.assertEqual(atbat_action.event, 'Wild Pitch')
                    self.assertEqual(atbat_action.event_es, 'Lanzamiento Descontrolado')
                    self.assertEqual(atbat_action.event_num, 229)
                    self.assertEqual(atbat_action.home_team_runs, 2)
                    self.assertEqual(atbat_action.o, 2)
                    self.assertEqual(atbat_action.pitch, 4)
                    self.assertEqual(atbat_action.player, 425766)
                    self.assertEqual(atbat_action.play_guid, '79d308c3-585d-4473-82ac-9e1a311f26a1')
                    self.assertEqual(atbat_action.s, 2)
                    self.assertEqual(atbat_action.tfs, 2130)
                    self.assertEqual(atbat_action.tfs_zulu, '2016-08-03T00:21:30Z')
                    self.assertEqual(atbat_action.__str__(), 'With Michael Conforto batting, wild pitch by Masahiro Tanaka, James Loney to 2nd.  ')
                # atbat specific tests
                if isinstance(atbat_action, AtBat):
                    self.assertIsInstance(atbat_action.b1, (int, str))
                    self.assertIsInstance(atbat_action.b2, (int, str))
                    self.assertIsInstance(atbat_action.b3, (int, str))
                    self.assertIsInstance(atbat_action.batter, int)
                    self.assertIsInstance(atbat_action.num, int)
                    self.assertIsInstance(atbat_action.pitcher, int)
                    self.assertIsInstance(atbat_action.pitches, list)
                    self.assertIsInstance(atbat_action.start_tfs, int)
                    self.assertIsInstance(atbat_action.start_tfs_zulu, str)
                    for pitch in atbat_action.pitches:
                        self.assertIsInstance(pitch.des, str)
                        try:
                            self.assertIsInstance(pitch.des_es, (unicode, str))
                        except NameError:
                            self.assertIsInstance(pitch.des_es, str)
                        self.assertIsInstance(pitch.pitch_type, str)
                        self.assertIsInstance(pitch.start_speed, float)
                        self.assertIsInstance(pitch.sv_id, (str, int))
                        self.assertIsInstance(pitch.type, str)
                # action specific tests
                if isinstance(atbat_action, Action):
                    self.assertIsInstance(atbat_action.pitch, int)
                    self.assertIsInstance(atbat_action.player, int)
                    self.assertIsInstance(atbat_action.tfs, int)
                    self.assertIsInstance(atbat_action.tfs_zulu, str)
                # mutual tests
                self.assertIsInstance(atbat_action.away_team_runs, int)
                self.assertIsInstance(atbat_action.b, int)
                self.assertIsInstance(atbat_action.des, str)
                try:
                    self.assertIsInstance(atbat_action.des_es, (unicode, str))
                except NameError:
                    self.assertIsInstance(atbat_action.des_es, str)
                self.assertIsInstance(atbat_action.event, str)
                try:
                    self.assertIsInstance(atbat_action.event_es, (unicode, str))
                except NameError:
                    self.assertIsInstance(atbat_action.event_es, str)
                self.assertIsInstance(atbat_action.event_num, int)
                self.assertIsInstance(atbat_action.home_team_runs, int)
                self.assertIsInstance(atbat_action.o, int)
                self.assertIsInstance(atbat_action.play_guid, str)
                self.assertIsInstance(atbat_action.s, int)

    def test_game_events_empty(self):
        self.assertRaises(ValueError, lambda: mlbgame.game_events('game_id'))
        self.assertRaises(ValueError, lambda: mlbgame.game_events('2016_08_02_nymlb_nymlb_1'))
