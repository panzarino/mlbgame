#!/usr/bin/env python

import unittest

import mlbgame


class TestEvents(unittest.TestCase):

    def test_game_events(self):
        events = mlbgame.game_events('2016_08_02_nyamlb_nynmlb_1')
        for inning in events:
            self.assertIsInstance(inning.num, int)
            if inning.num == 1:
                i = inning
            self.assertIsInstance(inning.top, list)
            self.assertIsInstance(inning.bottom, list)
            atbats = inning.top + inning.bottom
            for atbat in atbats:
                if inning.num == 1 and atbat.num == 1:
                    ab = atbat
                self.assertIsInstance(atbat.away_team_runs, int)
                self.assertIsInstance(atbat.b, int)
                self.assertIsInstance(atbat.b1, (int, str))
                self.assertIsInstance(atbat.b2, (int, str))
                self.assertIsInstance(atbat.b3, (int, str))
                self.assertIsInstance(atbat.batter, int)
                self.assertIsInstance(atbat.des, str)
                try:
                    self.assertIsInstance(atbat.des_es, (unicode, str))
                except NameError:
                    self.assertIsInstance(atbat.des_es, str)
                self.assertIsInstance(atbat.event, str)
                try:
                    self.assertIsInstance(atbat.event_es, (unicode, str))
                except NameError:
                    self.assertIsInstance(atbat.event_es, str)
                self.assertIsInstance(atbat.event_num, int)
                self.assertIsInstance(atbat.home_team_runs, int)
                self.assertIsInstance(atbat.num, int)
                self.assertIsInstance(atbat.o, int)
                self.assertIsInstance(atbat.pitcher, int)
                self.assertIsInstance(atbat.pitches, list)
                self.assertIsInstance(atbat.play_guid, str)
                self.assertIsInstance(atbat.s, int)
                self.assertIsInstance(atbat.start_tfs, int)
                self.assertIsInstance(atbat.start_tfs_zulu, str)
                for pitch in atbat.pitches:
                    self.assertIsInstance(pitch.des, str)
                    try:
                        self.assertIsInstance(pitch.des_es, (unicode, str))
                    except NameError:
                        self.assertIsInstance(pitch.des_es, str)
                    self.assertIsInstance(pitch.pitch_type, str)
                    self.assertIsInstance(pitch.start_speed, float)
                    self.assertIsInstance(pitch.sv_id, (str, int))
                    self.assertIsInstance(pitch.type, str)
        inning = i
        self.assertEqual(inning.num, 1)
        self.assertEqual(inning.__str__(), 'Inning 1')
        atbat = ab
        self.assertEqual(atbat.away_team_runs, 0)
        self.assertEqual(atbat.b, 1)
        self.assertEqual(atbat.b1, '')
        self.assertEqual(atbat.b2, '')
        self.assertEqual(atbat.b3, '')
        self.assertEqual(atbat.batter, 458731)
        self.assertEqual(atbat.des, 'Brett Gardner flies out to center fielder Alejandro De Aza.  ')
        self.assertEqual(atbat.des_es, 'Brett Gardner batea elevado de out a jardinero central Alejandro De Aza.  ')
        self.assertEqual(atbat.event, 'Flyout')
        self.assertEqual(atbat.event_es, 'Elevado de Out')
        self.assertEqual(atbat.event_num, 6)
        self.assertEqual(atbat.home_team_runs, 0)
        self.assertEqual(atbat.num, 1)
        self.assertEqual(atbat.o, 1)
        self.assertEqual(atbat.pitcher, 594798)
        self.assertEqual(atbat.play_guid, 'e91fe0bf-6e1e-40a3-953c-47a943b37638')
        self.assertEqual(atbat.s, 0)
        self.assertEqual(atbat.start_tfs, 231105)
        self.assertEqual(atbat.start_tfs_zulu, '2016-08-02T23:11:05Z')
        self.assertEqual(atbat.__str__(), 'Brett Gardner flies out to center fielder Alejandro De Aza.  ')
        pitch = atbat.pitches[0]
        self.assertEqual(pitch.des, 'Ball')
        self.assertEqual(pitch.des_es, 'Bola mala')
        self.assertEqual(pitch.pitch_type, 'FT')
        self.assertEqual(pitch.start_speed, 95.2)
        self.assertEqual(pitch.type, 'B')
        self.assertEqual(pitch.__str__(), 'Pitch: FT at 95.2: Ball')

    def test_game_events_empty(self):
        self.assertRaises(ValueError, lambda: mlbgame.game_events('game_id'))
        self.assertRaises(ValueError, lambda: mlbgame.game_events('2016_08_02_nymlb_nymlb_1'))
