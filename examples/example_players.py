#!/usr/bin/env python

import mlbgame
import re

def rename(name):
    return re.sub(r'_', ' ', name).title()

game = mlbgame.day(2017, 7, 9, away='Orioles')[0]
players = mlbgame.players(game.game_id)

print(game.home_team + ' vs ' + game.away_team + ' (' + str(game.date) + ')')

types = ['home', 'away']
for type in types:
    print('  ' + getattr(game, type + '_team') + ' Information:')
    team_players = getattr(players, type + '_players')
    team_coaches = getattr(players, type + '_coaches')

    print('    Coaching Staff:')
    for coach in team_coaches:
        print('      {0}: {first} {last}'.format(rename(coach['position']), **coach))

    print('    Starting Lineup:')
    starting_lineup = list(filter(lambda x: 'bat_order' in x.keys(), team_players))
    for player in sorted(starting_lineup, key=lambda k: k['bat_order']):
        print('      {bat_order}. {first} {last} ({game_position})'.format(**player))

print('  Umpires:')
for umpire in players.umpires:
    print('      {0}: {first} {last}'.format(rename(umpire['position']), **umpire))

"""
Twins vs Orioles (2017-07-09 13:10:00)
  Twins Information:
    Coaching Staff:
      Manager: Paul Molitor
      Hitting Coach: James Rowson
      Assistant Hitting Coach: Rudy Hernandez
      Pitching Coach: Neil Allen
      First Base Coach: Jeff Smith
      Third Base Coach: Gene Glynn
      Bench Coach: Joe Vavra
      Bullpen Coach: Eddie Guardado
      Major League Coach: Jeff Pickler
      Bullpen Catcher: Nate Dammann
    Starting Lineup:
      0. Kyle Gibson (P)
      1. Brian Dozier (2B)
      2. Robbie Grossman (DH)
      3. Max Kepler (RF)
      4. Miguel Sano (3B)
      5. Kennys Vargas (1B)
      6. Eddie Rosario (LF)
      7. Jorge Polanco (SS)
      8. Chris Gimenez (C)
      9. Zack Granite (CF)
  Orioles Information:
    Coaching Staff:
      Manager: Buck Showalter
      Hitting Coach: Scott Coolbaugh
      Assistant Hitting Coach: Howie Clark
      Pitching Coach: Roger McDowell
      First Base Coach: Wayne Kirby
      Third Base Coach: Bobby Dickerson
      Bench Coach: John Russell
      Bullpen Coach: Alan Mills
      Coach: Einar Diaz
    Starting Lineup:
      0. Ubaldo Jimenez (P)
      1. Seth Smith (RF)
      2. Manny Machado (3B)
      3. Jonathan Schoop (2B)
      4. Adam Jones (CF)
      5. Mark Trumbo (DH)
      6. Trey Mancini (1B)
      7. Hyun Soo Kim (LF)
      8. Caleb Joseph (C)
      9. Ruben Tejada (SS)
  Umpires:
      Home: Lance Barrett
      First: Bill Welke
      Second: Jim Reynolds
      Third: Sean Barber
"""