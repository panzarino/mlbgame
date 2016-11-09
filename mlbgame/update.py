#!/usr/bin/env python

from __future__ import print_function

import mlbgame

from datetime import date, timedelta
import getopt
import gzip
import os
import shutil
import sys

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

def date_usage():
    """Display usage of dates."""
    print("Something was wrong with your date(s): Dates must be correct and in the format <MM-DD-YYYY>. End date cannot be before start date.")

def run(hide=False, stats=False, events=False, overview=False, start=date(2012, 1, 12), end=None):
    """Update local game data."""
    # set end to be the day before today at maximum
    today = date.today()
    if end == None or end >= today:
        end =  today - timedelta(days=1)
    # check if the dates are in correct chronological order
    if start > end:
        date_usage()
        sys.exit(2)
    # print a message becuase sometimes it seems like the program is not doing anything
    if not hide:
        print("Checking local data...")
    # get information for loop
    d = start
    delta = timedelta(days=1)
    # calculate the days between the start and the end
    difference = float((end - start).days + .0)
    # loop through the dates
    while d <= end:
        i = d.year
        x = d.month
        y = d.day
        monthstr = str(x).zfill(2)
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
            try:
                # get data from url
                data = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/scoreboard.xml" % (i, monthstr, daystr))
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
        # get stats if specified
        if stats:
            try:
                # get the data for games on this day
                games = mlbgame.day(i, x, y)
                for z in games:
                    # get the game id which is used to fetch data
                    game_id = z.game_id
                    # file information
                    filename2 = "gameday-data/year_%i/month_%s/day_%s/gid_%s/boxscore.xml.gz" % (i, monthstr, daystr, game_id)
                    f2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename2)
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
            except:
                pass
        # get events if specified
        if events:
            try:
                # get the data for games on this day
                games = mlbgame.day(i, x, y)
                for z in games:
                    # get the game id which is used to fetch data
                    game_id = z.game_id
                    # file information
                    filename3 = "gameday-data/year_%i/month_%s/day_%s/gid_%s/game_events.xml.gz" % (i, monthstr, daystr, game_id)
                    f3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename3)
                    dirn3 = "gameday-data/year_%i/month_%s/day_%s/gid_%s" % (i, monthstr, daystr, game_id)
                    dirname3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirn3)
                    if not os.path.isfile(f3):
                        # try because some dates may not have a file on the mlb.com server
                        # or some months don't have a 31st day
                        try:
                            # get data
                            data3 = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/gid_%s/game_events.xml" % (i, monthstr, daystr, game_id))
                            response3 = data3.read()
                            # checking if files exist and writing new files
                            if not os.path.exists(dirname3):
                                try:
                                    os.makedirs(dirname3)
                                except OSError:
                                    access_error(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))
                            # try to write file
                            try:
                                with gzip.open(f3, "w") as fi:
                                    fi.write(response3)
                            except OSError:
                                access_error(dirname3)
                        except HTTPError:
                            pass
            except:
                pass
        # get overview if specified
        if overview:
            try:
                # get the data for games on this day
                games = mlbgame.day(i, x, y)
                for z in games:
                    # get the game id which is used to fetch data
                    game_id = z.game_id
                    # file information
                    filename4 = "gameday-data/year_%i/month_%s/day_%s/gid_%s/linescore.xml.gz" % (i, monthstr, daystr, game_id)
                    f4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename4)
                    dirn4 = "gameday-data/year_%i/month_%s/day_%s/gid_%s" % (i, monthstr, daystr, game_id)
                    dirname4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirn4)
                    # check if file exists
                    # aka is the information saved
                    if not os.path.isfile(f4):
                        # try because some dates may not have a file on the mlb.com server
                        # or some months don't have a 31st day
                        try:
                            # get data
                            data4 = urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/gid_%s/linescore.xml" % (i, monthstr, daystr, game_id))
                            response4 = data4.read()
                            # checking if files exist and writing new files
                            if not os.path.exists(dirname4):
                                try:
                                    os.makedirs(dirname4)
                                except OSError:
                                    access_error(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))
                            # try to write file
                            try:
                                with gzip.open(f4, "w") as fi:
                                    fi.write(response4)
                            except OSError:
                                access_error(dirname4)
                        except HTTPError:
                            pass
            except:
                pass
        # loading message to show something is actually happening
        if not hide:
            sys.stdout.write('Loading games (%00.2f%%) \r' % ((1-((end - d).days/difference))*100))
            sys.stdout.flush()
        # increment the date counter
        d += delta

    if not hide:
        # make sure loading ends at 100%
        sys.stdout.write('Loading games (100.00%).\n')
        sys.stdout.flush()
        # show finished message
        print("Complete.")

def clear():
    """Delete all cached data"""
    try:
        shutil.rmtree(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))
    except OSError:
        access_error(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gameday-data/'))

def usage():
    """Display usage of command line arguments."""
    print("usage: "+sys.argv[0]+" <arguments>")
    print()
    print("Arguments:")
    print("--help (-h)\t\t\tdisplay this help menu")
    print("--clear\t\t\t\tdelete all cached data")
    print("--hide\t\t\t\thides output from update script")
    print("--stats\t\t\t\tsaves the box scores and individual game stats from every game")
    print("--events\t\t\tsaves the game events from every game")
    print("--overview\t\t\tsaves the game overview from every game")
    print("--start (-s) <MM-DD-YYYY>\tdate to start updating from (default: 01-01-2012)")
    print("--end (-e) <MM-DD-YYYY>\t\tdate to update until (default: current day)")

def start():
    """Start updating from a command and arguments."""
    try:
        data = getopt.getopt(sys.argv[1:], "hms:e:", ["help", "clear", "hide", "stats", "events", "overview", "start=", "end="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    hide = False
    more = False
    stats = False
    events = False
    overview = False
    start = "01-01-2012"
    today = date.today()
    end = "%i-%i-%i" % (today.month, today.day, today.year)
    # parse arguments
    for x in data[0]:
        if x[0] == "-h" or x[0] == "--help":
            return usage()
        elif x[0] == "--clear":
            return clear()
        elif x[0] == "--hide":
            hide = True
        elif x[0] == "--stats":
            stats = True
        elif x[0] == "--events":
            events = True
        elif x[0] == "--overview":
            overview = True
        elif x[0] == "-s" or x[0] == "--start":
            start = x[1]
        elif x[0] == "-e" or x[0] == "--end":
            end = x[1]
    # verify that dates are acceptable
    try:
        # split argument
        split_start = start.split("-")
        split_end = end.split("-")
        # create example dates
        date_start = date(int(split_start[2]), int(split_start[0]), int(split_start[1]))
        date_end = date(int(split_end[2]), int(split_end[0]), int(split_end[1]))
    except:
        date_usage()
        sys.exit(2)
    run(hide, stats, events, overview, date_start, date_end)
    
# start program when run from command line
if __name__ == "__main__":
    start()
