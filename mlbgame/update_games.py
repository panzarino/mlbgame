import urllib2 as url
import os
import sys
from datetime import date
import gzip
import mlbgame
import getopt

def run(hide=False, extra=False, start_date=2012):
    '''
    Update local game data
    '''
    year = date.today().year
    month = date.today().month
    day = date.today().day
    if not hide:
        print "Checking data..."
    for i in range(start_date, year+1):
        for x in range(1, 13):
            monthstr = str(x).zfill(2)
            loading = False
            if i == year and x > month:
                break
            for y in range(1, 31):
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
    print "-h (--help)\t\tdisplay this help menu"
    print "--hide\t\t\thides output from update script"
    print "--extra\t\t\tsaves the box scores and individual game stats from every game"
    print "--start_date <year>\tyear to start updating from (runs until current day)"

def start():
    try:
        data = getopt.getopt(sys.argv[1:], "h", ["help", "hide", "extra", "start_date="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    hide = False
    extra = False
    start_date = 2012
    for x in data[0]:
        if x[0] == "-h" or x[0] == "--help":
            usage()
            sys.exit()
        elif x[0] == "--hide":
            hide = True
        elif x[0] == "--extra":
            extra = True
        elif x[0] == "--start_date":
            start_date = int(x[1])
    run(hide, extra, start_date)
    

if __name__ == "__main__":
    start()