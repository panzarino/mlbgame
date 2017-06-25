#!/usr/bin/env python

from tabulate import tabulate
from mlbgame import standings

s = standings.Standings()

for division in s.divisions:
    print division.name
    division_standings = []
    for team in division.standings:
        team_standings = [team.team_short, team.w, team.l, team.pct, team.gb,
                team.last_ten, team.streak, team.home, team.away]
        division_standings.append(team_standings)
    print tabulate(division_standings,
            headers=['', 'W', 'L', 'PCT', 'GB', 'L10', 'STRK', 'HOME', 'ROAD'])
    print
print 'Last Updated: %s' % s.last_update
