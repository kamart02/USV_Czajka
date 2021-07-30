import requests
import json

from requests.api import head

URL = 'http://192.168.33.6:8000/api'

def removeData():
    try:
        req = requests.get('{}/data/'.format(URL))
        if req.json():
            for element in req.json():
                requests.delete('{}/data/{}'.format(URL, element['id']))
        else:
            return False
    except:
        print("Error while removing data")

def removeMapData():
    try:
        req = requests.get('{}/mapdata/'.format(URL))
        if req.json():
            for element in req.json():
                requests.delete('{}/mapdata/{}'.format(URL, element['id']))
        else:
            return False
    except:
        print("Error while removing map data")

def initSpeed():
    try:
        req = requests.get('{}/speed/'.format(URL))
        if req.json():
            if len(req.json())>1:
                for element in req.json():
                    requests.delete('{}/speed/{}'.format(URL, element['id']))
                requests.post('{}/speed/'.format(URL), 
                data=json.dumps(
                    {
                        'rightSpeed': 0,
                        'leftSpeed':0
                    }),
                headers={'Content-Type':'application/json'},)
        else:
            requests.post('{}/speed/'.format(URL), 
                data=json.dumps(
                    {
                        'rightSpeed': 0,
                        'leftSpeed':0
                    }),
                headers={'Content-Type':'application/json'},)
    except:
        print("Error while initSpeed")

def clearStatus():
    try:
        req = requests.get('{}/status/'.format(URL))
        if req.json():
            for element in req.json():
                requests.delete('{}/status/{}'.format(URL, element['id']))
        else:
            return False
    except:
        print("Error while clearing status")

def deletAllWaypoints():
    try:
        req = requests.get('{}/waypoint/'.format(URL))
        if req.json():
            for element in req.json():
                requests.delete('{}/waypointN/'.format(URL),
                data=json.dumps(
                    {
                        'all': True
                    }
                ),
                headers={'Content-Type':'application/json'})
        else:
            return False
    except:
        print("Error while deleting all waypoints")


def getOneWaypoint():
    try:
        req = requests.get('{}/waypointN/'.format(URL))
        if req.json():
            return req.json()
        else:
            return False
    except:
        print("Error while getting one waypoint")

def deleteFirstWaypoint():
    try:
        wp = getOneWaypoint()
        requests.delete('{}/waypoint/'.format(URL), 
        data=json.dumps({
            'all': False
        }),
        headers={'Content-Type':'application/json'})
    except:
        print("Error while removing first waypoint")

def getSpeed():
    try:
        req = requests.get('{}/speed/'.format(URL))
        return req.json()[-1]
    except:
        print("Error while getting speed")

def updateSpeed(speed):
    try:
        #lastSpeed = getSpeed()
        requests.put('{}/speedU/'.format(URL), 
            data=json.dumps(
                {
                    'rightSpeed': speed['right'],
                    'leftSpeed': speed['left'],
                }),
            headers={'Content-Type':'application/json'},)
    except:
        print("Error while updating speed")

def updateData(data):
    try:
        requests.post('{}/data/'.format(URL), 
            data=json.dumps(
                {
                    'ph': data['ph'],
                    'turbility': data['turbility'],
                    'temperature':data['temperature'],
                    'latitude':data['latitude'],
                    'longitude':data['longitude'],
                    'voltage':data['voltageBatt']

                }),
            headers={'Content-Type':'application/json'},)
    except:
        print("Error while updating data")

def updateMapData(data):
    try:
        requests.post('{}/mapdata/'.format(URL), 
            data=json.dumps(
                {
                    'ph': data['ph'],
                    'turbility': data['turbility'],
                    'temperature':data['temperature'],
                    'latitude':data['latitude'],
                    'longitude':data['longitude']

                }),
            headers={'Content-Type':'application/json'},)
    except:
        print("Error while updating map data")

def getStatus():
    try:
        req = requests.get('{}/status/'.format(URL))
        if req.json():
            return req.json()[-1]
        else:
            return False
    except:
        print("Error while getting status")

#not working anymore
def updateAbort(val):
    try:
        requests.put('{}/abort/'.format(URL),
            data = json.dumps(
                {
                    'abort': val,
                }),
            headers={'Content-Type':'application/json'},
        )
    except:
        print("Error while updating abort")
    

#temporary

def getShutdown():
    return False
