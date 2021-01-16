import api
import auto
import time

#import gpio

lastUpdate = time.time()

def getGPS():
    return {
        'longitude': 0,
        'latitude': 0
    }

def getCompass():
    return 0

def updateEngine(speed):
    pass

def shutdown():
    pass

def readData():
    pass

def sendData():
    if(time.time()-lastUpdate>=1):
        pass

def sendMapData():
    pass
    
def start():
    while True:
        if api.getShutdown():
            shutdown()

        if api.getAbort():
            updateEngine({
                'leftSpeed': 0,
                'rightSpeed': 0
            })

        if api.getOneWaypoint()!=False:
            auto.start()
            

        updateEngine(api.getSpeed())

        sendData()

    


