import urllib2 as url
import xml.etree.ElementTree as etree

data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_2015/month_08/day_01/scoreboard.xml")
data = etree.parse(data)
root = data.getroot()
games = []
for game in root:
    games.append(game)