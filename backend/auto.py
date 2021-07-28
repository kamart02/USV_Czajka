import math
from geopy import distance

degreeThreshold = 10
distanceThreashold = 2

autoEngineSpeedStop = {
    'leftSpeed': 0,
    'rightSpeed': 0
}

autoEngineSpeedCW = {
    'leftSpeed': 10,
    'rightSpeed': -10
}

autoEngineSpeedCCW = {
    'leftSpeed': -10,
    'rightSpeed': 10
}

autoEngineSpeedDrive = {
    'leftSpeed': 30,
    'rightSpeed': 30
}

autoEngineSpeedDriveCW = {
    'leftSpeed': 30,
    'rightSpeed': 20
}

autoEngineSpeedDriveCCW = {
    'leftSpeed': 20,
    'rightSpeed': 30
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



def start(waypoint, compassBearing, GPS):
    
    #print(waypoint['longitude'])
    waypoint['longitude']=float(waypoint['longitude'])
    waypoint['latitude']=float(waypoint['latitude'])

    pos = GPS
    currentBearing = compassBearing
    targetBearing = calculateBearing(pos['longitude'], pos['latitude'], waypoint['longitude'], waypoint['latitude'])

    if getDir(currentBearing, targetBearing)['amount']<=degreeThreshold:
        return autoEngineSpeedStop, True

    if getDir(currentBearing, targetBearing)['dir']=='CW':
        return autoEngineSpeedCW, False
        #main.updateEngine(autoEngineSpeedCW)
    else:
        return autoEngineSpeedCCW, False
        #main.updateEngine(autoEngineSpeedCCW)

def move(waypoint, compassBearing, GPS):
        waypoint['longitude']=float(waypoint['longitude'])
        waypoint['latitude']=float(waypoint['latitude'])
        pos = GPS
        currentBearing = compassBearing
        targetBearing = calculateBearing(pos['longitude'], pos['latitude'],waypoint['longitude'], waypoint['latitude'])

        if distance.distance((pos['longitude'], pos['latitude']),(waypoint['longitude'], waypoint['latitude']))<distanceThreashold:
            return autoEngineSpeedStop, True

        if getDir(currentBearing, targetBearing)['amount'] <= degreeThreshold:
            return autoEngineSpeedDrive, False
        else:
            if getDir(currentBearing, targetBearing)['dir'] =='CW':
                return autoEngineSpeedDriveCW, False
            else: 
                return autoEngineSpeedDriveCCW, False




#54.539423, 17.747500
#54.540139, 17.748634