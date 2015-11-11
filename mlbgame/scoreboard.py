import urllib2 as url
import xml.etree.ElementTree as etree

def scoreboard(year, month, day):
    monthstr = str(month)
    daystr = str(day)
    if month < 10:
        monthstr = "0"+str(month)
    if day < 10:
        daystr = "0"+str(day)
    data = url.urlopen("http://gd2.mlb.com/components/game/mlb/year_"+str(year)+"/month_"+monthstr+"/day_"+daystr+"/scoreboard.xml")
    data = etree.parse(data)
    root = data.getroot()
    games = {}
    for game in root:
        if game.tag == "go_game":
            game_type = "go_game"
            game_data = game.find('game')
            game_id = game_data.attrib['id']
            game_league = game_data.attrib['league']
            game_status = game_data.attrib['status']
            game_start_time = game_data.attrib['start_time']
            teams = game.findall('team')
            home_team_data = teams[0].find('gameteam')
            home_team = {'name': teams[0].attrib['name'], 'runs': home_team_data.attrib['R'], 'hits':home_team_data.attrib['H'], 'errors':home_team_data.attrib['E']}
            away_team_data = teams[1].find('gameteam')
            away_team = {'name': teams[1].attrib['name'], 'runs': away_team_data.attrib['R'], 'hits':away_team_data.attrib['H'], 'errors':away_team_data.attrib['E']}
            w_pitcher_data = game.find('w_pitcher')
            w_pitcher_name = w_pitcher_data.find('pitcher').attrib['name']
            w_pitcher = {'name':w_pitcher_name, 'wins':w_pitcher_data.attrib['wins'], 'losses':w_pitcher_data.attrib['losses']}
            l_pitcher_data = game.find('l_pitcher')
            l_pitcher_name = l_pitcher_data.find('pitcher').attrib['name']
            l_pitcher = {'name':l_pitcher_name, 'wins':l_pitcher_data.attrib['wins'], 'losses':l_pitcher_data.attrib['losses']}
            sv_pitcher_data = game.find('sv_pitcher')
            sv_pitcher_name = sv_pitcher_data.find('pitcher').attrib['name']
            sv_pitcher = {'name':sv_pitcher_name, 'saves':sv_pitcher_data.attrib['saves']}
            output = {'game_type':game_type, 'game_league':game_league, 'game_status':game_status, 'game_start_time':game_start_time, 'home_team':home_team, 'away_team':away_team, 'w_pitcher':w_pitcher, 'l_pitcher':l_pitcher, 'sv_pitcher':sv_pitcher}
            games[game_id]=output
        elif game.tag == "sg_game":
            game_type = "sg_game"
            game_data = game.find('game')
            game_id = game_data.attrib['id']
            game_league = game_data.attrib['league']
            game_status = game_data.attrib['status']
            game_start_time = game_data.attrib['start_time']
            delay_reason = game_data.find('delay_reason').text
            teams = game.findall('team')
            home_team_data = teams[0].find('gameteam')
            home_team = {'name': teams[0].attrib['name'], 'runs': home_team_data.attrib['R'], 'hits':home_team_data.attrib['H'], 'errors':home_team_data.attrib['E']}
            away_team_data = teams[1].find('gameteam')
            away_team = {'name': teams[1].attrib['name'], 'runs': away_team_data.attrib['R'], 'hits':away_team_data.attrib['H'], 'errors':away_team_data.attrib['E']}
            output = {'game_type':game_type, 'game_league':game_league, 'game_status':game_status, 'game_start_time':game_start_time, 'home_team':home_team, 'away_team':away_team, 'delay_reason':delay_reason}
            games[game_id]=output
    return games

class Game(object):
    '''
    Game object to hold information about a certain game
    '''
    def __init__(self, data):
        