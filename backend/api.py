import requests
import json

from requests.api import head

URL = 'http://192.168.33.6:8000/api'

def removeData():
    req = requests.get('{}/data/'.format(URL))
    if req.json():
        for element in req.json():
            requests.delete('{}/data/{}'.format(URL, element['id']))
    else:
        return False

def removeMapData():
    req = requests.get('{}/mapdata/'.format(URL))
    if req.json():
        for element in req.json():
            requests.delete('{}/mapdata/{}'.format(URL, element['id']))
    else:
        return False

def initSpeed():
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

def clearStatus():
    req = requests.get('{}/status/'.format(URL))
    if req.json():
        for element in req.json():
            requests.delete('{}/status/{}'.format(URL, element['id']))
    else:
        return False

def deletAllWaypoints():
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


def getOneWaypoint():
    req = requests.get('{}/waypointN/'.format(URL))
    if req.json():
        return req.json()
    else:
        return False

def deleteFirstWaypoint():
    wp = getOneWaypoint()
    requests.delete('{}/waypoint/'.format(URL), 
    data=json.dumps({
        'all': False
    }),
    headers={'Content-Type':'application/json'})

def getSpeed():
    req = requests.get('{}/speed/'.format(URL))
    return req.json()[-1]

def updateSpeed(speed):
    #lastSpeed = getSpeed()
    requests.put('{}/speedU/'.format(URL), 
        data=json.dumps(
            {
                'rightSpeed': speed['right'],
                'leftSpeed': speed['left'],
            }),
        headers={'Content-Type':'application/json'},)

def updateData(data):
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

def updateMapData(data):
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

def getStatus():
    req = requests.get('{}/status/'.format(URL))
    if req.json():
        return req.json()[-1]
    else:
        return False

#not working anymore
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
