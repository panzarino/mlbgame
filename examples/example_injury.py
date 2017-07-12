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

# Astros               Updated    Status     Due Back                   Injury                                Notes
# -------------------  ---------  ---------  -------------------------  ------------------------------------  --------------------------------------------------------------------------------------------
# Musgrove, Joe (P)    06/09      10-day DL  Likely June 12             Right shoulder discomfort             Threw bullpen session June 8; played catch June 9.
# Morton, Charlie (P)  06/09      10-day DL  TBD                        Right lat strain                      Shut down as of May 31 update; threw from 75 feet June 9.
# McHugh, Collin (P)   06/08      60-day DL  TBD                        Posterior impingement in right elbow  Doing light mound work per May 31 update; may throw breaking pitches soon per June 5 update.
# Keuchel, Dallas (P)  06/10      10-day DL  Possibly mid-to-late June  Neck discomfort                       MRI revealed inflammation, will not throw for roughly one week as of June 10 update.
# Gustave, Jandel (P)  05/31      10-day DL  TBD                        Right forearm tightness               Participating in throwing program in Florida as of May 31 update.
#
# Last Updated: 2017-06-11 06:56:50
