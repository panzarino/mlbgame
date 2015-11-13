import urllib2 as url
import os

def run():
    for i in range(2012, 2015):
        for x in range(1, 13):
            print '\rLoading games for %d/%d' % (x, i)
            for y in range(1, 31):
                monthstr = str(x).zfill(2)
                daystr = str(y).zfill(2)
                filename = "gameday-data/year_"+str(i)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml.gz"
                file = os.path.join(os.path.dirname(__file__), filename)
                if not os.path.isfile(file):
                    try:
                        data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_"+str(i)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml")
                        response = data.read()
                        dirn = "gameday-data/year_"+str(i)+"/month_"+monthstr+"/day_"+daystr
                        dirname = os.path.join(os.path.dirname(__file__), dirn)
                        if not os.path.exists(dirname):
                            os.makedirs(dirname)
                        with open(file, "w") as f:
                            f.write(response)
                    except url.HTTPError:
                        pass