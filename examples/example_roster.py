#!/usr/bin/env python

from tabulate import tabulate
from mlbgame import roster
import dateutil.parser
from datetime import datetime

team_id = 117 # Houston Astros
r = roster.Roster(team_id)
mlbroster = []

for player in r.roster:
    birth_date = dateutil.parser.parse(player.birth_date)
    dob = birth_date.strftime('%m/%d/%Y')
    player = [player.jersey_number, player.name_display_first_last,
        '%s/%s' % (player.bats, player.throws),
        '%s\'%s"' % (player.height_feet, player.height_inches), player.weight,
        dob]
    mlbroster.append(player)
print tabulate(mlbroster, headers=['#', 'Name', 'B/T', 'Ht', 'Wt', 'DOB'])
print
print 'Last Updated: %s' % r.last_update


#   #  Name                 B/T    Ht       Wt  DOB
# ---  -------------------  -----  -----  ----  ----------
#  27  Jose Altuve          R/R    5'6"    165  05/06/1990
#   3  Norichika Aoki       L/R    5'9"    180  01/05/1982
#  80  Andrew Aplin         L/L    6'0"    205  03/21/1991
#  15  Carlos Beltran       S/R    6'1"    215  04/24/1977
#   2  Alex Bregman         R/R    6'0"    180  03/30/1994
#   1  Carlos Correa        R/R    6'4"    215  09/22/1994
#  47  Chris Devenski       R/R    6'3"    210  11/13/1990
#  38  Dayan Diaz           R/R    5'10"   195  02/10/1989
#  45  Michael Feliz        R/R    6'4"    230  06/28/1993
#  54  Mike Fiers           R/R    6'2"    200  06/15/1985
#  11  Evan Gattis          R/R    6'4"    270  08/18/1986
#  53  Ken Giles            R/R    6'2"    205  09/20/1990
#   9  Marwin Gonzalez      S/R    6'1"    205  03/14/1989
#  44  Luke Gregerson       L/R    6'3"    205  05/14/1984
#  64  Reymin Guduan        L/L    6'4"    205  03/16/1992
#  10  Yuli Gurriel         R/R    6'0"    190  06/09/1984
#  61  Jandel Gustave       R/R    6'2"    210  10/12/1992
#  36  Will Harris          R/R    6'4"    250  08/28/1984
#  35  Teoscar Hernandez    R/R    6'2"    180  10/15/1992
#  51  James Hoyt           R/R    6'6"    230  09/30/1986
#  18  Tony Kemp            L/R    5'6"    165  10/31/1991
#  60  Dallas Keuchel       L/L    6'3"    205  01/01/1988
#   6  Jake Marisnick       R/R    6'4"    220  03/30/1991
#  16  Brian McCann         L/R    6'3"    225  02/20/1984
#  43  Lance McCullers Jr.  L/R    6'1"    205  10/02/1993
#  31  Collin McHugh        R/R    6'2"    190  06/19/1987
#  19  Colin Moran          L/R    6'4"    204  10/01/1992
#  50  Charlie Morton       R/R    6'5"    235  11/12/1983
#  59  Joe Musgrove         R/R    6'5"    265  12/04/1992
#  63  David Paulino        R/R    6'7"    215  02/06/1994
#  41  Brad Peacock         R/R    6'1"    210  02/02/1988
#  22  Josh Reddick         L/R    6'2"    195  02/19/1987
#  23  A.J. Reed            L/L    6'4"    275  05/10/1993
#  62  Brady Rodgers        R/R    6'2"    210  09/17/1990
#  29  Tony Sipp            L/L    6'0"    190  07/12/1983
#   4  George Springer      R/R    6'3"    215  09/19/1989
#  46  Ashur Tolliver       L/L    6'0"    170  01/24/1988
#  20  Preston Tucker       L/L    6'0"    215  07/06/1990
#  13  Tyler White          R/R    5'11"   225  10/29/1990
#
#  Last Updated: 2017-05-16 02:13:15
