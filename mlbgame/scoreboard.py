import urllib2 as url
import xml.etree.ElementTree as etree

def scoreboard(year, month, day):
    if month < 10:
        monthstr = "0"+str(month)
    if day < 10:
        daystr = "0"+str(day)
    data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_"+str(year)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml")
    data = etree.parse(data)
    root = data.getroot()
    games = []
    for game in root:
        games.append(game)
    return games