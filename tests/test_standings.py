#!/usr/bin/env python
import pytest
from datetime import datetime
from mlbgame import standings



date = datetime(2017, 5, 15, 19, 4, 59, 367187)
s = standings.Standings(date)

def test_standings_url():
    standings_url = 'http://mlb.mlb.com/lookup/json/named.standings_schedule_date.bam?season=2017&' \
         'schedule_game_date.game_date=%272017/05/15%27&sit_code=%27h0%27&league_id=103&' \
         'league_id=104&all_star_sw=%27N%27&version=2'
    assert s.standings_url == standings_url


def test_historical_standings_url():
    date = datetime(2016, 5, 15)
    s = standings.Standings(date)
    standings_url = 'http://mlb.mlb.com/lookup/json/named.historical_standings_schedule_date.bam?season=2016&' \
            'game_date=%272016/05/15%27&sit_code=%27h0%27&league_id=103&league_id=104&' \
            'all_star_sw=%27N%27&version=48'
    assert s.standings_url == standings_url


def test_divisions_is_list():
    assert type(s.divisions) is list
