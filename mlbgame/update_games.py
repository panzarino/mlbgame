import urllib2 as url
import os
import sys
from datetime import date
import gzip

def run(hide=False):
    '''
    Update local game data
    '''
    year = date.today().year
    month = date.today().month
    day = date.today().day
    for i in range(2012, year+1):
        for x in range(1, 13):
            monthstr = str(x).zfill(2)
            loading = False
            if i == year and x > month:
                break
            for y in range(1, 31):
                if i == year and x >= month and y >= day:
                    break
                daystr = str(y).zfill(2)
                filename = "gameday-data/year_"+str(i)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml.gz"
                f = os.path.join(os.path.dirname(__file__), filename)
                dirn = "gameday-data/year_"+str(i)+"/month_"+monthstr+"/day_"+daystr
                dirname = os.path.join(os.path.dirname(__file__), dirn)
                if not os.path.isfile(f):
                    try:
                        data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_"+str(i)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml")
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
                            with gzip.open(f, "w") as f:
                                f.write(response)
                        except OSError:
                            print 'I do not have write access to "%s".' % dirname
                            print 'Without write access, I cannot update the game database.'
                            sys.exit(1)
                    except url.HTTPError:
                        pass
            if loading and not hide:
                sys.stdout.write('Loading games for %s-%d (100.00%%)\n' % (monthstr, i))
                sys.stdout.flush()
    if not hide:
        print "Complete"

if __name__ == "__main__":
    run()