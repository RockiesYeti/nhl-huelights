
import requests
import json
import time
from siren import sirenLight

def game_live(gameid, teamid):
    cur_goal=0
    game_is_on=True
    while game_is_on:
        game_response = requests.get('https://statsapi.web.nhl.com/api/v1/game/'+gameid+'/feed/live')
        game=json.loads(game_response.text)
        if game['liveData']['linescore']['teams']['home']['team']['id']==teamid:
            if game['liveData']['linescore']['teams']['home']['goals'] > cur_goal:
                print("We Scored!!")
                sirenLight()
                cur_goal=game['liveData']['linescore']['teams']['home']['goals']
        else:
            if game['liveData']['linescore']['teams']['away']['goals'] > cur_goal:
                print("We Scored!!")
                sirenLight()
                cur_goal=game['liveData']['linescore']['teams']['away']['goals']
        if int(game['liveData']['linescore']['currentPeriod']) > 0 and int(game['gameData']['status']['codedGameState']) < 7:
            game_is_on=True
        else:
            game_is_on=False
        time.sleep(10)