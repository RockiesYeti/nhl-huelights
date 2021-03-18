
import requests
import json
import time
import argparse
import sys
from siren import sirenLight
from pregame import pregame
from game_live import game_live


parser = argparse.ArgumentParser(description='Runs my huelights when the team scores')
parser.add_argument('team', metavar='teamname', type=str)
args = parser.parse_args()
team = args.team
teams_response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
teams=json.loads(teams_response.text)
for i in range(len(teams['teams'])):
    if team == teams['teams'][i]['name']:
        teamid=str(teams['teams'][i]['id'])
        break
if teamid is None:
    print("Invalid Teamname")
    exit

sched_response = requests.get('https://statsapi.web.nhl.com/api/v1/schedule?teamId='+teamid)
sched=json.loads(sched_response.text)
if len(sched['dates']) != 0:
    gameid=str(sched['dates'][0]['games'][0]['gamePk'])
    pregame(gameid)
    game_live(gameid, teamid)
else:
    print("No Game Scheduled for "+team)
    



