#!/usr/bin/env python

import unittest
import requests_mock
import requests
import json
from datetime import datetime
import dateutil.parser
from mlbgame import standings

class TestStandings(unittest.TestCase):
    def setUp(self):
        self.date = datetime.now()
        self.hist_date = datetime(2016, 6, 2)
        self.standings_file = 'files/standings.json'
        self.hist_standings_file = 'files/historical_standings.json'
        self.standings_url = ''.join([
            'http://mlb.mlb.com/lookup/json/',
            'named.standings_schedule_date.bam',
            '?season={0}&schedule_game_date'.format(self.date.year),
            '.game_date=%27{0}%27&'.format(self.date.strftime('%Y/%m/%d')),
            'sit_code=%27h0%27&league_id=103&league_id=104&',
            'all_star_sw=%27N%27&version=2'])
        self.hist_standings_url = ''.join([
            'http://mlb.mlb.com/lookup/json/',
            'named.historical_standings_schedule_date.bam',
            '?season={0}&'.format(self.hist_date.year),
            'game_date=%27{0}%27&'.format(self.hist_date.strftime('%Y/%m/%d')),
            'sit_code=%27h0%27&league_id=103&league_id=104&'
            'all_star_sw=%27N%27&version=48'])
        with open(self.standings_file) as json_data:
            self.standings_json = json.load(json_data)
            json_data.close()

    def tearDown(self):
        del self.date
        del self.standings_file
        del self.hist_standings_file
        del self.hist_date
        del self.standings_url
        del self.hist_standings_url
        del self.standings_json

    def test_standings_url(self):
        s = standings.Standings(self.date)
        self.assertEqual(s.standings_url, self.standings_url)

    def test_historical_standings_url(self):
        s = standings.Standings(self.hist_date)
        self.assertEqual(s.standings_url, self.hist_standings_url)

    @requests_mock.Mocker()
    def test_divisions_is_list(self, mock_requests):
        mock_requests.get(self.standings_url, json=self.standings_json)
        s = standings.Standings(self.date)
        self.assertIsInstance(s.divisions, list)

    @requests_mock.Mocker()
    def test_standings_json(self, mock_requests):
        mock_requests.get(self.standings_url, json=self.standings_json)
        s = standings.Standings(self.date)
        self.assertEqual(s.standings_json, self.standings_json)

    @requests_mock.Mocker()
    def test_last_update(self, mock_requests):
        mock_requests.get(self.standings_url, json=self.standings_json)
        s = standings.Standings(self.date)
        last_update = self.standings_json['standings_schedule_date']\
            ['standings_all_date_rptr']['standings_all_date']\
            [0]['queryResults']['created']
        self.assertEqual(dateutil.parser.parse(last_update), s.last_update)
