import requests
import json
import time

def pregame(gameid):
    pregame=True
    game_response = requests.get('https://statsapi.web.nhl.com/api/v1/game/'+gameid+'/feed/live')
    game=json.loads(game_response.text)
    print("{} at {} ".format(game['gameData']['teams']['away']['name'],game['gameData']['teams']['home']['name']))
    while pregame:
        game_response = requests.get('https://statsapi.web.nhl.com/api/v1/game/'+gameid+'/feed/live')
        game=json.loads(game_response.text)
        sec_gametime=time.mktime(time.strptime(game['gameData']['datetime']['dateTime'],"%Y-%m-%dT%H:%M:%SZ"))-time.mktime(time.gmtime())
        hours_gametime=int(sec_gametime/3600)
        mins_gametime=int((sec_gametime%3600)/60)
        secs_gametime=int((sec_gametime%3600)%60)
        print("{} hours {} min {} sec until Puck Drop".format(hours_gametime,mins_gametime,secs_gametime ))
        if  int(game['gameData']['status']['codedGameState']) > 2 and int(game['gameData']['status']['codedGameState']) < 7:
            pregame=False
            game_is_on=True
        else:
            pregame=True
            game_is_on=False
            time.sleep(300)