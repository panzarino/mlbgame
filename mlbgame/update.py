#!/usr/bin/env python

from __future__ import print_function
import os
import sys
from datetime import date
import gzip
import mlbgame
import getopt
try:
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import urlopen, HTTPError


def access_error(name):
    """Display error message when program cannot write to file."""
    print('I do not have write access to "%s".' % (name))
    print('Without write access, I cannot update the game database.')
    sys.exit(1)

def run(hide=False, more=False, start="01-01-2012", end=None):
    """Update local game data."""
    # get today's information
    year = date.today().year
    month = date.today().month
    day = date.today().day
    # get ending date information
    if end != None:
        end_month, end_day, end_year = end.split("-")
        end_month, end_day, end_year = [int(end_month), int(end_day), int(end_year)]
    else:
        end_year = year
        end_month = month
        end_day = day
    # get starting date information
    start_month, start_day, start_year = start.split("-")
    first_day, first_month, last_month = [True, True, False]
    # print a message becuase sometimes it seems like the program is not doing anything
    if not hide:
        print("Checking local data...")
    # looping years
    for i in range(int(start_year), end_year+1):
        # checking if starting month value needs to be used
        if first_month:
            ms = int(start_month)
            first_month = False
        else:
            ms = 1
        # looping months
        me = 13
        if i == end_year:
            me = end_month+1
            last_month = True
        for x in range(ms, me):
            monthstr = str(x).zfill(2)
            loading = False
            if i == year and x > month:
                break
            # checking if starting day value needs to be used
            if first_day:
                ds = int(start_day)
                first_day = False
            else:
                ds = 1
            # looping days
            de = 32
            if last_month:
                de = end_day+1
            for y in range(ds, de):
                if i == year and x >= month and y >= day:
                    break
                daystr = str(y).zfill(2)
                # file information
                filename = "gameday-data/year_%i/month_%s/day_%s/scoreboard.xml.gz" % (i, monthstr, daystr)
                f = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
                dirn = "gameday-data/year_%i/month_%s/day_%s" % (i, monthstr, daystr)
                dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirn)
                # check if file exists
                # aka is the data saved
                if not os.path.isfile(f):
                    # try becuase some dates may not have a file on the mlb.com server
                    # or some months don't have a 31st day
                    try:
                        # get data from url
                        data = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/scoreboard.xml" % (i, monthstr, daystr))
                        # loading bar to show something is actually happening
                        if not hide:
                            sys.stdout.write('Loading games for %s-%d (%00.2f%%) \r' % (monthstr, i, y/31.0*100))
                            sys.stdout.flush()
                        loading = True
                        response = data.read()
                        # check if the path exists where the file should go
                        if not os.path.exists(dirname):
                            try:
                                # try to make the folder if permissions allow
                                os.makedirs(dirname)
                            except OSError:
                                access_error(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))
                        try:
                            # try to create the file if permissions allow
                            with gzip.open(f, "w") as fi:
                                fi.write(response)
                        except OSError:
                            access_error(dirname)
                    # do nothing if the file is not on mlb.com
                    except HTTPError:
                        pass
                # get extra data if specified
                if more:
                    try:
                        # get the data for games on this day
                        games = mlbgame.day(i, x, y)
                        for z in games:
                            # get the game id which is used to fetch data
                            game_id = z.game_id
                            # file information
                            filename2 = "gameday-data/year_%i/month_%s/day_%s/gid_%s/boxscore.xml.gz" % (i, monthstr, daystr, game_id)
                            filename3 = "gameday-data/year_%i/month_%s/day_%s/gid_%s/game_events.xml.gz" % (i, monthstr, daystr, game_id)
                            f2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename2)
                            f3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename3)
                            dirn2 = "gameday-data/year_%i/month_%s/day_%s/gid_%s" % (i, monthstr, daystr, game_id)
                            dirname2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirn2)
                            # check if file exists
                            # aka is the information saved
                            if not os.path.isfile(f2):
                                # try because some dates may not have a file on the mlb.com server
                                # or some months don't have a 31st day
                                try:
                                    # get data
                                    data2 = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/gid_%s/boxscore.xml" % (i, monthstr, daystr, game_id))
                                    response2 = data2.read()
                                    # checking if files exist and writing new files
                                    if not os.path.exists(dirname2):
                                        try:
                                            os.makedirs(dirname2)
                                        except OSError:
                                            access_error(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))
                                    # try to write file
                                    try:
                                        with gzip.open(f2, "w") as fi:
                                            fi.write(response2)
                                    except OSError:
                                        access_error(dirname2)
                                except HTTPError:
                                    pass
                            # check if file exists
                            # aka is the information saved
                            if not os.path.isfile(f3):
                                # try because some dates may not have a file on the mlb.com server
                                # or some months don't have a 31st day
                                try:
                                    # get data
                                    data3 = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/gid_%s/boxscore.xml" % (i, monthstr, daystr, game_id))
                                    response3 = data3.read()
                                    # checking if files exist and writing new files
                                    if not os.path.exists(dirname2):
                                        try:
                                            os.makedirs(dirname2)
                                        except OSError:
                                            access_error(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))
                                    # try to write file
                                    try:
                                        with gzip.open(f3, "w") as fi:
                                            fi.write(response3)
                                    except OSError:
                                        access_error(dirname2)
                                except HTTPError:
                                    pass
                    except:
                        pass
            if loading and not hide:
                # make sure loading ends at 100%
                sys.stdout.write('Loading games for %s-%d (100.00%%).\n' % (monthstr, i))
                sys.stdout.flush()
    # print finished message
    if not hide:
        print("Complete.")

def usage():
    """Display usage of command line arguments."""
    print("usage: "+sys.argv[0]+" <arguments>")
    print()
    print( "Arguments:")
    print( "--help (-h)\t\t\tdisplay this help menu")
    print( "--hide\t\t\t\thides output from update script")
    print( "--more (-m)\t\t\tsaves the box scores and individual game stats from every game")
    print( "--start (-s) <MM-DD-YYYY>\tdate to start updating from (default: 01-01-2012)")
    print( "--end (-e) <MM-DD-YYYY>\t\tdate to update until (default: current day)")

def date_usage():
    """Display usage of dates."""
    print("Something was wrong with your date(s): Dates must be correct and in the format <MM-DD-YYYY>")

def start():
    """Start updating from a command and arguments."""
    try:
        data = getopt.getopt(sys.argv[1:], "hms:e:", ["help", "hide", "more", "start=", "end="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    hide = False
    more = False
    start = "01-01-2012"
    today = date.today()
    end = "%i-%i-%i" % (today.month, today.day, today.year)
    # parse arguments
    for x in data[0]:
        if x[0] == "-h" or x[0] == "--help":
            usage()
            sys.exit()
        elif x[0] == "--hide":
            hide = True
        elif x[0] == "-m" or x[0] == "--more":
            more = True
        elif x[0] == "-s" or x[0] == "--start":
            start = x[1]
        elif x[0] == "-e" or x[0] == "--end":
            end = x[1]
    # verify that dates are acceptable
    try:
        # split argument
        split = start.split("-")
        split2 = end.split("-")
        # create example dates
        date1 = date(int(split[2]), int(split[0]), int(split[1]))
        date2 = date(int(split2[2]), int(split2[0]), int(split2[1]))
        # verify dates
        if date1 > date2 or date1 >= today or date2 > today:
            date_usage()
            sys.exit(2)
    except:
        date_usage()
        sys.exit(2)
    run(hide, more, start, end)
    
# start program when run from command line
if __name__ == "__main__":
    start()
