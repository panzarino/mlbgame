#!/usr/bin/env python

from tabulate import tabulate
from mlbgame import injury
import dateutil.parser
from datetime import datetime

team_id = 117 # Houston Astros
i = injury.Injury(team_id)
injuries = []

for inj in i.injuries:
    team = inj.team_name
    injury = ['{0}, {1} ({2})'.format(inj.name_last, inj.name_first,
        inj.position), inj.insert_ts, inj.injury_status, inj.due_back,
        inj.injury_desc, inj.injury_update]
    injuries.append(injury)
print tabulate(injuries, headers=[team, 'Updated', 'Status', 'Due Back',
    'Injury', 'Notes'])
print
print 'Last Updated: %s' % i.last_update

"""
"""
