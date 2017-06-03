#!/usr/bin/env python
import unittest
import requests_mock
import requests
import json
from datetime import datetime
import dateutil.parser
from mlbgame import roster

class TestRoster(unittest.TestCase):
    def setUp(self):
        self.team_id = 117
        base_url = 'http://mlb.mlb.com'
        self.roster_url = '%s/lookup/json/named.roster_40.bam?team_id=%s' % \
            (base_url, self.team_id)
        self.roster_file = 'files/roster.json'
        with open(self.roster_file) as json_data:
            self.roster_json = json.load(json_data)
            json_data.close()

    def tearDown(self):
        del self.team_id
        del self.roster_url
        del self.roster_file
        del self.roster_json

    def test_roster_url(self):
        r = roster.Roster(self.team_id)
        self.assertEqual(r.roster_url, self.roster_url)

    def test_roster_is_list(self):
        r = roster.Roster(self.team_id)
        self.assertIsInstance(r.roster, list)

    @requests_mock.Mocker()
    def test_roster_json(self, requests_mock):
        requests_mock.get(self.roster_url, json=self.roster_json)
        r = roster.Roster(self.team_id)
        self.assertEqual(r.roster_json, self.roster_json)

    @requests_mock.Mocker()
    def test_last_update(self, requests_mock):
        requests_mock.get(self.roster_url, json=self.roster_json)
        r = roster.Roster(self.team_id)
        last_update = self.roster_json['roster_40']['queryResults']['created']
        self.assertEqual(dateutil.parser.parse(last_update), r.last_update)
