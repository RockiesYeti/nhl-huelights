
import requests
import json
import time
from siren import sirenLight
from pregame import pregame
from game_live import game_live


sched_response = requests.get('https://statsapi.web.nhl.com/api/v1/schedule?teamId=21')
sched=json.loads(sched_response.text)
gameid=str(sched['dates'][0]['games'][0]['gamePk'])
pregame(gameid)
game_live(gameid)



