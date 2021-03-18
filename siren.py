import requests
import json
import time
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def sirenLight(color):
    body={
    "on": True
    }
    putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/4/state", json.dumps(body), verify=False)
    putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/5/state", json.dumps(body), verify=False)
    putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/14/state", json.dumps(body), verify=False)
    for i in range(0,10):
        if i%2==0:
            body={
                "hue": color
            }
        else:
            body={
                "hue": 8217
            }
        putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/4/state", json.dumps(body), verify=False)
        putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/5/state", json.dumps(body), verify=False)
        putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/14/state", json.dumps(body), verify=False)
        time.sleep(1)
    body={
        "hue": 8217
    }
    putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/4/state", json.dumps(body), verify=False)
    putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/5/state", json.dumps(body), verify=False)
    putr=requests.put("https://192.168.86.25/api/asmfBcBwWVeC9IpGjfXLaz6tKGAGIrp2QJkJOKwe/lights/14/state", json.dumps(body), verify=False)
