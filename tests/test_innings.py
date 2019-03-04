#!/usr/bin/env python

import unittest

import mlbgame


class TestInnings(unittest.TestCase):

    def _assert_stringlike(self, value):
        try:
            self.assertIsInstance(value, (unicode, str))
        except NameError:
            self.assertIsInstance(value, str)

    def test_game_innings(self):
        innings = mlbgame.game_events('2016_08_02_nyamlb_nynmlb_1', True)
        for inning in innings:
            self.assertIsInstance(inning.num, int)
            if inning.num == 1:
                i = inning
            self.assertIsInstance(inning.top, list)
            self.assertIsInstance(inning.bottom, list)
            atbats = inning.top + inning.bottom
            for atbat in atbats:
                if inning.num == 1 and atbat.num == 1:
                    ab = atbat
                # TODO: distinguish assertions on AtBat and Action objects
                # some of the assertions test attributes specific to AtBats,
                # so we need to skip Actions.
                if not isinstance(atbat, mlbgame.events.AtBat):
                    continue
                self.assertIsInstance(atbat.away_team_runs, int)
                self.assertIsInstance(atbat.b, int)
                self.assertIsInstance(atbat.batter, int)
                self.assertIsInstance(atbat.stand, str)
                self.assertIsInstance(atbat.b_height,(str,int))
                self.assertIsInstance(atbat.des, str)
                self._assert_stringlike(atbat.des_es)
                self.assertIsInstance(atbat.event, str)
                self._assert_stringlike(atbat.event_es)
                self.assertIsInstance(atbat.event_num, int)
                self.assertIsInstance(atbat.home_team_runs, int)
                self.assertIsInstance(atbat.num, int)
                self.assertIsInstance(atbat.o, int)
                self.assertIsInstance(atbat.pitcher, int)
                self.assertIsInstance(atbat.p_throws, str)
                self.assertIsInstance(atbat.pitches, list)
                self.assertIsInstance(atbat.play_guid, str)
                self.assertIsInstance(atbat.s, int)
                self.assertIsInstance(atbat.start_tfs, int)
                self.assertIsInstance(atbat.start_tfs_zulu, str)
                for pitch in atbat.pitches:
                    self.assertIsInstance(pitch.des, str)
                    self._assert_stringlike(pitch.des_es)
                    self.assertIsInstance(pitch.id, int)
                    self.assertIsInstance(pitch.type, str)
                    self.assertIsInstance(pitch.code, str)
                    self.assertIsInstance(pitch.tfs, int)
                    self.assertIsInstance(pitch.tfs_zulu, str)
                    self.assertIsInstance(pitch.x, (int, float))
                    self.assertIsInstance(pitch.y, (int, float))
                    self.assertIsInstance(pitch.event_num, int)
                    self.assertIsInstance(pitch.sv_id, (str, int))
                    self.assertIsInstance(pitch.play_guid, str)
                    self.assertIsInstance(pitch.start_speed, (int, float))
                    self.assertIsInstance(pitch.end_speed, (int, float))
                    self.assertIsInstance(pitch.sz_top, (int, float))
                    self.assertIsInstance(pitch.sz_bot, (int, float))
                    self.assertIsInstance(pitch.pfx_x, (int, float))
                    self.assertIsInstance(pitch.pfx_z, (int, float))
                    self.assertIsInstance(pitch.px, (int, float))
                    self.assertIsInstance(pitch.pz, (int, float))
                    self.assertIsInstance(pitch.x0, (int, float))
                    self.assertIsInstance(pitch.y0, (int, float))
                    self.assertIsInstance(pitch.z0, (int, float))
                    self.assertIsInstance(pitch.vx0, (int, float))
                    self.assertIsInstance(pitch.vy0, (int, float))
                    self.assertIsInstance(pitch.vz0, (int, float))
                    self.assertIsInstance(pitch.ax, (int, float))
                    self.assertIsInstance(pitch.ay, (int, float))
                    self.assertIsInstance(pitch.az, (int, float))
                    self.assertIsInstance(pitch.break_y, float)
                    self.assertIsInstance(pitch.break_angle, float)
                    self.assertIsInstance(pitch.break_length, float)
                    self.assertIsInstance(pitch.pitch_type, str)
                    self.assertIsInstance(pitch.type_confidence, float)
                    self.assertIsInstance(pitch.zone, int)
                    self.assertIsInstance(pitch.nasty, int)
                    self.assertIsInstance(pitch.spin_dir, float)
                    self.assertIsInstance(pitch.spin_rate, float)
                    self.assertIsInstance(pitch.cc, str)
                    self.assertIsInstance(pitch.mt, str)
        inning = i
        self.assertEqual(inning.num, 1)
        self.assertEqual(inning.__str__(), 'Inning 1')
        atbat = ab
        self.assertEqual(atbat.away_team_runs, 0)
        self.assertEqual(atbat.b, 1)
        self.assertEqual(atbat.batter, 458731)
        self.assertEqual(atbat.stand, 'L')
        self.assertEqual(atbat.b_height, '5-11')
        self.assertEqual(atbat.des, 'Brett Gardner flies out to center fielder Alejandro De Aza.  ')
        self.assertEqual(atbat.des_es, 'Brett Gardner batea elevado de out a jardinero central Alejandro De Aza.  ')
        self.assertEqual(atbat.event, 'Flyout')
        self.assertEqual(atbat.event_es, 'Elevado de Out')
        self.assertEqual(atbat.event_num, 6)
        self.assertEqual(atbat.home_team_runs, 0)
        self.assertEqual(atbat.num, 1)
        self.assertEqual(atbat.o, 1)
        self.assertEqual(atbat.pitcher, 594798)
        self.assertEqual(atbat.p_throws, 'R')
        self.assertEqual(atbat.play_guid, 'e91fe0bf-6e1e-40a3-953c-47a943b37638')
        self.assertEqual(atbat.s, 0)
        self.assertEqual(atbat.start_tfs, 231105)
        self.assertEqual(atbat.start_tfs_zulu, '2016-08-02T23:11:05Z')
        self.assertEqual(atbat.__str__(), 'Brett Gardner flies out to center fielder Alejandro De Aza.  ')
        pitch = atbat.pitches[0]
        self.assertEqual(pitch.des, 'Ball')
        self.assertEqual(pitch.des_es, 'Bola mala')
        self.assertEqual(pitch.id, 3)
        self.assertEqual(pitch.type, 'B')
        self.assertEqual(pitch.code, 'B')
        self.assertEqual(pitch.tfs, 231122)
        self.assertEqual(pitch.tfs_zulu, "2016-08-02T23:11:22Z")
        self.assertEqual(pitch.x, 161.25)
        self.assertEqual(pitch.y, 143.42)
        self.assertEqual(pitch.event_num, 3)
        # test below reflects differing behavior of mlbgame.object.setobjattr
        # returns the string in Python < 3.6 and the int in 3.6+
        self.assertIn(pitch.sv_id, (160802191259, "160802_191259"))
        self.assertEqual(pitch.play_guid, "daeb229c-f106-4360-a7ea-08d4da117424")
        self.assertEqual(pitch.start_speed, 95.2)
        self.assertEqual(pitch.end_speed, 86.8)
        self.assertEqual(pitch.sz_top, 3.08)
        self.assertEqual(pitch.sz_bot, 1.46)
        self.assertEqual(pitch.pfx_x, -7.67)
        self.assertEqual(pitch.pfx_z, 7.29)
        self.assertEqual(pitch.px, -1.161)
        self.assertEqual(pitch.pz, 3.532)
        self.assertEqual(pitch.x0, -1.053)
        self.assertEqual(pitch.y0, 50)
        self.assertEqual(pitch.z0, 5.601)
        self.assertEqual(pitch.vx0, 2.432)
        self.assertEqual(pitch.vy0, -139.644)
        self.assertEqual(pitch.vz0, -2.417)
        self.assertEqual(pitch.ax, -14.963)
        self.assertEqual(pitch.ay, 34.94)
        self.assertEqual(pitch.az, -17.886)
        self.assertEqual(pitch.break_y, 23.7)
        self.assertEqual(pitch.break_angle, 37.8)
        self.assertEqual(pitch.break_length, 4.9)
        self.assertEqual(pitch.pitch_type, "FT")
        self.assertEqual(pitch.type_confidence, .913)
        self.assertEqual(pitch.zone, 11)
        self.assertEqual(pitch.nasty, 56)
        self.assertEqual(pitch.spin_dir, 226.321)
        self.assertEqual(pitch.spin_rate, 2149.420)
        self.assertEqual(pitch.cc, "")
        self.assertEqual(pitch.mt, "")
        self.assertEqual(pitch.__str__(), 'Pitch: FT at 95.2: Ball')

    def test_game_innings_empty(self):
        self.assertRaises(ValueError, lambda: mlbgame.game_events('game_id', True))
        self.assertRaises(ValueError, lambda: mlbgame.game_events('2016_08_02_nymlb_nymlb_1', True))
