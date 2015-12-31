import urllib2 as url
import os
import sys
from datetime import date
import gzip
import mlbgame
import getopt

def run(hide=False, extra=False, start_date="01-01-2012"):
    '''
    Update local game data
    '''
    year = date.today().year
    month = date.today().month
    day = date.today().day
    start_month, start_day, start_year = start_date.split("-")
    first_day, first_month = [True, True]
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
            for y in range(ds, 31):
                if i == year and x >= month and y >= day:
                    break
                daystr = str(y).zfill(2)
                filename = "gameday-data/year_%i/month_%s/day_%s/scoreboard.xml.gz" % (i, monthstr, daystr)
                f = os.path.join(os.path.dirname(__file__), filename)
                dirn = "gameday-data/year_%i/month_%s/day_%s" % (i, monthstr, daystr)
                dirname = os.path.join(os.path.dirname(__file__), dirn)
                if not os.path.isfile(f):
                    try:
                        data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/scoreboard.xml" % (i, monthstr, daystr))
                        if not hide:
                            sys.stdout.write('Loading games for %s-%d (%00.2f%%) \r' % (monthstr, i, y/31.0*100))
                            sys.stdout.flush()
                        loading = True
                        response = data.read()
                        if not os.path.exists(dirname):
                            try:
                                os.makedirs(dirname)
                            except OSError:
                                print 'I do not have write access to "%s".' % (os.path.join(os.path.dirname(__file__), 'gameday-data/'))
                                print 'Without write access, I cannot update the game database.'
                                sys.exit(1)
                        try:
                            with gzip.open(f, "w") as fi:
                                fi.write(response)
                        except OSError:
                            print 'I do not have write access to "%s".' % dirname
                            print 'Without write access, I cannot update the game database.'
                            sys.exit(1)
                    except url.HTTPError:
                        pass
                if extra:
                    try:
                        games = mlbgame.day(i, x, y)
                        for z in games:
                            game_id = z.game_id
                            filename2 = "gameday-data/year_%i/month_%s/day_%s/gid_%s/boxscore.xml.gz" % (i, monthstr, daystr, game_id)
                            f2 = os.path.join(os.path.dirname(__file__), filename2)
                            dirn2 = "gameday-data/year_%i/month_%s/day_%s/gid_%s" % (i, monthstr, daystr, game_id)
                            dirname2 = os.path.join(os.path.dirname(__file__), dirn2)
                            if not os.path.isfile(f2):
                                try:
                                    data2 = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_%i/month_%s/day_%s/gid_%s/boxscore.xml" % (i, monthstr, daystr, game_id))
                                    if not hide:
                                        sys.stdout.write('Loading games for %s-%d (%00.2f%%). \r' % (monthstr, i, y/31.0*100))
                                        sys.stdout.flush()
                                    loading = True
                                    response2 = data2.read()
                                    if not os.path.exists(dirname2):
                                        try:
                                            os.makedirs(dirname2)
                                        except OSError:
                                            print 'I do not have write access to "%s".' % (os.path.join(os.path.dirname(__file__), 'gameday-data/'))
                                            print 'Without write access, I cannot update the game database.'
                                            sys.exit(1)
                                    try:
                                        with gzip.open(f2, "w") as fi:
                                            fi.write(response2)
                                    except OSError:
                                        print 'I do not have write access to "%s".' % dirname2
                                        print 'Without write access, I cannot update the game database.'
                                        sys.exit(1)
                                except url.HTTPError:
                                    pass
                    except:
                        pass
            if loading and not hide:
                sys.stdout.write('Loading games for %s-%d (100.00%%).\n' % (monthstr, i))
                sys.stdout.flush()
    if not hide:
        print "Complete."

def usage():
    print "usage: "+sys.argv[0]+" <arguments>"
    print
    print "Arguments:"
    print "--help (-h)\t\t\tdisplay this help menu"
    print "--hide\t\t\t\thides output from update script"
    print "--extra (-e)\t\t\tsaves the box scores and individual game stats from every game"
    print "--start_date (-s) <MM-DD-YYYY>\tdate to start updating from (runs until current day)"

def start():
    try:
        data = getopt.getopt(sys.argv[1:], "hes:", ["help", "hide", "extra", "start_date="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    hide = False
    extra = False
    start_date = "01-01-2012"
    for x in data[0]:
        if x[0] == "-h" or x[0] == "--help":
            usage()
            sys.exit()
        elif x[0] == "--hide":
            hide = True
        elif x[0] == "-e" or x[0] == "--extra":
            extra = True
        elif x[0] == "-s" or x[0] == "--start_date":
            start_date = x[1]
    run(hide, extra, start_date)
    

if __name__ == "__main__":
    start()