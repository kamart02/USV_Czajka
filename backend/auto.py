
from webinterface.backend.main import sendData, sendMapData, updateEngine
from requests.api import get
import main
import api
import math
from geopy import distance

degreeThreshold = 10
distanceThreashold = 2

autoEngineSpeedCW = {
    'left': 10,
    'right': -10
}

autoEngineSpeedCCW = {
    'left': -10,
    'right': 10
}

autoEngineSpeedDrive = {
    'left': 30,
    'right': 30
}

autoEngineSpeedDriveCW = {
    'left': 30,
    'right': 20
}

autoEngineSpeedDriveCCW = {
    'left': 20,
    'right': 30
}

def calculateBearing(latOld, lngOld, latNew, lngNew):
    
    latOld = math.radians(latOld)
    lngOld = math.radians(lngOld)
    latNew = math.radians(latNew)
    lngNew = math.radians(lngNew)

    X = math.cos(latNew)*math.sin(lngNew-lngOld)
    Y = math.cos(latOld)*math.sin(latNew) - math.sin(latOld)*math.cos(latNew)*math.cos(lngNew-lngOld)

    return math.degrees(math.atan2(X, Y))

def getDir(currentBearing, targetBearing):
    if currentBearing<=targetBearing:
        amountCW = targetBearing - currentBearing
        amountCCW = currentBearing - targetBearing + 360
    else:
        amountCW = targetBearing - currentBearing + 360
        amountCCW = currentBearing - targetBearing 

    if(amountCW<=amountCCW):
        return {
            'dir': 'CW',
            'amount': amountCW
        }
    else:
        return {
            'dir': 'CCW',
            'amount': amountCCW
        }



def start():
    waypoint = 0
    abort = False
    while not abort:
        waypoint = api.getOneWaypoint()
        if waypoint == False:
            break
        while not abort:
            main.sendData()
            pos = main.getGPS()
            currentBearing = main.getCompass()
            targetBearing = calculateBearing(pos['longitude'], pos['latitude'],waypoint['longitude'], waypoint['latitude'])
            if getDir(currentBearing, targetBearing)['dir']=='CW':
                main.updateEngine(autoEngineSpeedCW)
            else:
                main.updateEngine(autoEngineSpeedCCW)
            if getDir(currentBearing, targetBearing)['amount']<=degreeThreshold:
                updateEngine({
                    'left': 0,
                    'right': 0
                })
                break
            abort = api.getAbort()
        while not abort:
            main.sendData()
            pos = main.getGPS()
            currentBearing = main.getCompass()
            targetBearing = calculateBearing(pos['longitude'], pos['latitude'],waypoint['longitude'], waypoint['latitude'])

            if distance.distance((pos['longitude'], pos['latitude']),(waypoint['longitude'], waypoint['latitude']).m)<distanceThreashold:
                updateEngine({
                    'left': 0,
                    'right': 0
                })
                sendMapData()
                break

            if getDir(currentBearing, targetBearing)['amount'] <= degreeThreshold:
                main.updateEngine(autoEngineSpeedDrive)
            else:
                if getDir(currentBearing, targetBearing)['dir'] =='CW':
                    main.updateEngine(autoEngineSpeedDriveCW)
                else: 
                    main.updateEngine(autoEngineSpeedCCW)
            
            abort = api.getAbort()




#54.539423, 17.747500
#54.540139, 17.748634