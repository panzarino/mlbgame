#!/usr/bin/env python
import pytest
from datetime import datetime
from mlbgame import roster

def test_roster_url():
    team_id = 117
    r = roster.Roster(team_id)
    roster_url = 'http://mlb.mlb.com/lookup/json/named.roster_40.bam?team_id=%s' % (team_id)
    assert r.roster_url == roster_url

def test_roster_is_list():
    team_id = 117
    r = roster.Roster(team_id)
    assert type(r.roster) is list
