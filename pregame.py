import requests
import json
import time

def pregame(gameid):
    pregame=True
    while pregame:
        print("Pregame loop: "+str(time.localtime()))
        game_response = requests.get('https://statsapi.web.nhl.com/api/v1/game/'+gameid+'/feed/live')
        game=json.loads(game_response.text)
        if  int(game['gameData']['status']['codedGameState']) > 2 and int(game['gameData']['status']['codedGameState']) < 7:
            pregame=False
            game_is_on=True
        else:
            pregame=True
            game_is_on=False
            time.sleep(300)