import urllib2 as url
import os
import sys
from datetime import date
import gzip
import mlbgame
import getopt

def access_error(name):
    '''
    Error message when program cannot write to file
    '''
    print 'I do not have write access to "%s".' % (name)
    print 'Without write access, I cannot update the game database.'
    sys.exit(1)

def run(hide=False, more=False, start="01-01-2012"):
    '''
    Update local game data
    '''
    # get today's information
    year = date.today().year
    month = date.today().month
    day = date.today().day
    # get starting date information
    start_month, start_day, start_year = start.split("-")
    first_day, first_month = [True, True]
    # print a message becuase sometimes it seems like the program is not doing anything
    if not hide:
        print "Checking local data..."
    # looping years
    for i in range(int(start_year), year+1):
        # checking if starting month value needs to be used
        if first_month:
            ms = int(start_month)
            first_month = False
        else:
            ms = 1
        # looping months
        for x in range(ms, 13):
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
            for y in range(ds, 32):
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
                        data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/scoreboard.xml" % (i, monthstr, daystr))
                        # loding bar to show something is actually happening
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
                    except url.HTTPError:
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
                            f2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename2)
                            dirn2 = "gameday-data/year_%i/month_%s/day_%s/gid_%s" % (i, monthstr, daystr, game_id)
                            dirname2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirn2)
                            # check if file exists
                            # aka is the information saved
                            if not os.path.isfile(f2):
                                # try becuase some dates may not have a file on the mlb.com server
                                # or some months don't have a 31st day
                                try:
                                    # get data
                                    data2 = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/gid_%s/boxscore.xml" % (i, monthstr, daystr, game_id))
                                    if not hide:
                                        # progress
                                        sys.stdout.write('Loading games for %s-%d (%00.2f%%). \r' % (monthstr, i, y/31.0*100))
                                        sys.stdout.flush()
                                    loading = True
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
                                except url.HTTPError:
                                    pass
                    except:
                        pass
            if loading and not hide:
                # make sure loading ends at 100%
                sys.stdout.write('Loading games for %s-%d (100.00%%).\n' % (monthstr, i))
                sys.stdout.flush()
    # print finished message
    if not hide:
        print "Complete."

def usage():
    '''
    Usage of command line arguments
    '''
    print "usage: "+sys.argv[0]+" <arguments>"
    print
    print "Arguments:"
    print "--help (-h)\t\t\tdisplay this help menu"
    print "--hide\t\t\t\thides output from update script"
    print "--more (-m)\t\t\tsaves the box scores and individual game stats from every game"
    print "--start (-s) <MM-DD-YYYY>\tdate to start updating from (runs until current day)"

def date_usage():
    print "Incorrect date: Dates must be correct and in the format <MM-DD-YYYY>"

def start():
    '''
    Start updating from a command and arguments
    '''
    try:
        data = getopt.getopt(sys.argv[1:], "hms:", ["help", "hide", "more", "start="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    hide = False
    more = False
    start = "01-01-2012"
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
    # verify that date is acceptable
    try:
        split = start.split("-")
        for x in split:
            int(x)
            if x<0:
                date_usage()
                sys.exit(2)
    except:
        date_usage()
        sys.exit(2)
    if len(split)!=3 or int(split[0])>12 or int(split[1])>31 or int(split[2])<1900 or int(split[2])>date.today().year:
            date_usage()
            sys.exit(2)
    run(hide, more, start)
    

if __name__ == "__main__":
    start()