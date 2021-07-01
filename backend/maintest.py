import requests
import json
import api

def checkStatus():
    status = api.getStatus()
    if status == False:
        return False
    else:
        if status['abort']==True:
            pass
        if status['delMapData']==True:
            api.removeMapData()
        if status['delData']==True:
            api.removeData()
        api.clearStatus()

while True:
    checkStatus()