import requests
import json

URL = 'http://127.0.0.1:8000/api'

def getOneWaypoint():
    req = requests.get('{}/waypoint/'.format(URL))
    if req.json():
        return req.json()[0]
    else:
        return False

def deleteFirstWaypoint():
    wp = getOneWaypoint()
    requests.delete('{}/waypoint/{}/'.format(URL, wp['id']))

def getSpeed():
    req = requests.get('{}/speed/'.format(URL))
    return req.json()[-1]

def updateSpeed(l, r):
    requests.put('{}/speed/1/'.format(URL), 
        data=json.dumps(
            {
                'rightSpeed': r,
                'leftSpeed': l,
            }),
        headers={'Content-Type':'application/json'},)

def updateData(data):
    requests.put('{}/data/'.format(URL), 
        data=json.dumps(
            {
                'ph': data['ph'],
                'turbility': data['turbility'],
                'temperature':data['temperature'],
                'latitude':data['latitude'],
                'longitude':data['longitude']

            }),
        headers={'Content-Type':'application/json'},)

def updateMapData(data):
    requests.put('{}/data/'.format(URL), 
        data=json.dumps(
            {
                'ph': data['ph'],
                'turbility': data['turbility'],
                'temperature':data['temperature'],
                'latitude':data['latitude'],
                'longitude':data['longitude']

            }),
        headers={'Content-Type':'application/json'},)

def getAbort():
    req = requests.get('{}/abort/'.format(URL))
    return req.json()[-1]['abort']

def updateAbort(val):
    requests.put('{}/abort/'.format(URL),
        data = json.dumps(
            {
                'abort': val,
            }),
        headers={'Content-Type':'application/json'},
    )
    

#temporary

def getShutdown():
    return False