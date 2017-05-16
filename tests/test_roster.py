#!/usr/bin/env python
import pytest
from datetime import datetime
from mlbgame import roster

team_id = 117
r = roster.Roster(team_id)

def test_roster_url():
    roster_url = 'http://mlb.mlb.com/lookup/json/named.roster_40.bam?team_id=117'
    assert r.roster_url == roster_url


def test_roster_is_list():
    assert type(r.roster) is list
