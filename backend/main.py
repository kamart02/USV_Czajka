#Main control code for drone. Consists of mostly data, status, speed updates. Also handles initialization.

#Important functions
#PH(voltage) -> y=-16.903313+7
#Turbility(voltage) -> y=-1120.4x^2 + 5742.3x - 4352.9

#Pinout
#17 - thermsensor (pin 4 broken)
#14 - GPS RX (UART TX)
#15 - GPS TX (UART RX)

#2 - I2C SDA
#3 - I2C SCL

#on arduino
#3 - reverse pin left
#4 - reverse pin right
#5 - drive pin left
#6 - drive pin right

#import of api file
import api
import auto

#import of required system libraries
import time
import os
import math

#import of GPS module
import gps

#import of ADC libraries
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#import of TempSensor libraries
from w1thermsensor import W1ThermSensor

#import of Compass
import adafruit_mlx90393

#import for EngineControler
from smbus import SMBus

#import of GPIO control and board constants
import gpiozero
import board
import busio


#constants

PHOFFSET=0

#Update Variables
lastUpdate = time.time()
lastCheck = time.time()
lastEngineUpdate = time.time()

#Sensor Variables
i2c = 0
adc = 0
therm = 0
compass = 0

#EngineControler variables
ControlerAddr = 0x38 # bus address
i2cbus = SMBus(1) # indicates /dev/ic2-1

#Engine wariables (WIP)
engineSpeed = {
    'left': 0,
    'right': 0
}

motorLeft = gpiozero.PhaseEnableMotor(27,23)
motorRight = gpiozero.PhaseEnableMotor(22,24)

#GPS variables
session = 0
longitude = 0
latitude = 0

#autoMode
isAuto=False
completedOneTrip=True
currentWaypoint=''


#function used to map values to other values
def mapVal(v, vl, vr, ol, orr):
        x = float(vr)-float(vl)
        y = float(v)/x
        z = float(orr)-float(ol)
        z*=y
        return z+ol

#reading GPS data
def getGPS():
    global longitude
    global latitude
    global session
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                longitude = report.lon
            if hasattr(report, 'lat'):
                latitude = report.lat
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")

    return {
        'longitude': longitude,
        'latitude': latitude
    }

#reading Compass data
def getCompass():
    MX, MY, MZ = compass.magnetic
    if MX==0:
        if MY<0:
            return 90.0
        else:
            return 0.0
    else:
        D = math.atan(MY/MX) * 180 / math.pi
        while D<0:
            D+=360
        while D>=360:
            D-=360
        return D

def sendEngineVal(leftSpeed, rightSpeed):
    i2cbus.write_byte(ControlerAddr, 202)
    i2cbus.write_byte(ControlerAddr,leftSpeed) # switch it on
    i2cbus.write_byte(ControlerAddr, 203)
    i2cbus.write_byte(ControlerAddr,rightSpeed) # switch it on

#updating engine speed and uploading it to database (needs changes)
def updateEngine(speed):
    
    if(engineSpeed['right']*speed['rightSpeed']<0 or engineSpeed['left']*speed['leftSpeed']<0 or (engineSpeed['right']<0 and speed['rightSpeed']==0) or (engineSpeed['left']<0 and speed['leftSpeed']==0)):
        if ((engineSpeed['right']>=0 and  engineSpeed['left']>=0)):
            engineSpeed['left']=0
            engineSpeed['right']=0

            sendEngineVal(0,0)
            time.sleep(0.5)
            
        elif (engineSpeed['right']<0 and  engineSpeed['left']>=0):
            engineSpeed['left']=0
            engineSpeed['right']=0

            sendEngineVal(0,101)
            time.sleep(0.5)
        elif (engineSpeed['right']>=0 and  engineSpeed['left']<0):
            engineSpeed['left']=0
            engineSpeed['right']=0

            sendEngineVal(101,0)
            time.sleep(0.5)
        elif (engineSpeed['right']<0 and  engineSpeed['left']<0):
            engineSpeed['left']=0
            engineSpeed['right']=0

            sendEngineVal(101,101)
            time.sleep(0.5)

        if (speed['rightSpeed']<0 and  speed['leftSpeed']<0):
            sendEngineVal(101,101)
            time.sleep(0.5)
        elif (speed['rightSpeed']>=0 and  speed['leftSpeed']<0):
            sendEngineVal(101,0)
            time.sleep(0.5)
        elif (speed['rightSpeed']<0 and  speed['leftSpeed']>=0):
            sendEngineVal(0,101)
            time.sleep(0.5)
        elif (speed['rightSpeed']>=0 and  speed['leftSpeed']>=0):
            sendEngineVal(0,0)
            time.sleep(0.5)

    

    engineSpeed['left'] = speed['leftSpeed']
    engineSpeed['right'] = speed['rightSpeed']

    temporaryEngineSpeedLeft = 0
    temporaryEngineSpeedRight = 0

    if engineSpeed['left']>=0:
        temporaryEngineSpeedLeft=engineSpeed['left']
        # motorLeft.forward(mapVal(engineSpeed['left'],0,100,0.4,0.9))
    else:
        temporaryEngineSpeedLeft=engineSpeed['left']*-1+101
        motorLeft.backward(mapVal(-1*engineSpeed['left'],0,100,0.4,0.9))

    if engineSpeed['right']>=0:
        temporaryEngineSpeedRight = engineSpeed['right']
        # motorRight.forward(mapVal(engineSpeed['right'],0,100,0.4,0.9))
    else:
        temporaryEngineSpeedRight = engineSpeed['right']*-1+101
        # motorRight.backward(mapVal(-1*engineSpeed['right'],0,100,0.4,0.9))
    #api.updateSpeed(engineSpeed)

    sendEngineVal(temporaryEngineSpeedLeft,temporaryEngineSpeedRight)

#wip
def shutdown():
    updateEngine({
        'left':0,
        'right':0
    })

#wip (missing voltage values)
def readData():
    ph = 0
    turbility = 0
    #analog 0 is ph and analog 1 is turbility
    ph = AnalogIn(adc, ADS.P0).voltage
    ph = ph*-16.903313 + 7 + PHOFFSET
    turbility = AnalogIn(adc, ADS.P1).voltage
    turbility = turbility * turbility * -1120.4 + turbility * 5742.3 - 4352.9
    temperature = therm.get_temperature()
    voltageBatt = AnalogIn(adc, ADS.P2).voltage
    voltageBatt *= 10.0*4980.0/1023.0

    return {
        'ph': ph,
        'turbility': turbility,
        'temperature': temperature,
        'voltageBatt': voltageBatt
    }

#wip (missing voltage values)
def sendData():
    global lastUpdate
    if(time.time()-lastUpdate>=5):
        lastUpdate = time.time()
        finalData = {
            'latitude': 0,
            'longitude': 0,
            'ph': 0,
            'turbility': 0,
            'temperature': 0
        }

        gpsData = getGPS()
        adcData = readData()
        #print(gpsData)
        finalData['latitude'] = gpsData['latitude']
        finalData['longitude'] = gpsData['longitude']
        finalData['turbility'] = round(adcData['turbility'],5)
        finalData['ph'] = round(adcData['ph'],5)
        finalData['temperature'] = round(adcData['temperature'],5)
        finalData['voltageBatt'] = round(adcData['voltageBatt'],5)

        api.updateData(finalData)

def sendMapData():
    finalData = {
            'latitude': 0,
            'longitude': 0,
            'ph': 0,
            'turbility': 0,
            'temperature': 0
        }

    gpsData = getGPS()
    adcData = readData()
    #print(gpsData)
    finalData['latitude'] = gpsData['latitude']
    finalData['longitude'] = gpsData['longitude']
    finalData['turbility'] = round(adcData['turbility'],5)
    finalData['ph'] = round(adcData['ph'],5)
    finalData['temperature'] = round(adcData['temperature'],5)

    api.updateMapData(finalData)

#initialization of ThermSensor
def initThermSenor():
    os.system("sudo modprobe w1-gpio")
    os.system("sudo modprobe w1-therm")
    os.system("sudo dtoverlay w1-gpio gpiopin=4 pullup=0")
    global therm
    therm = W1ThermSensor()

#initialization of GPS
def initGPS():
    #print('git')
    os.system("sudo gpsd /dev/serial0 -F /var/run/gpsd.sock")
    global session
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

#initialization of ADC
def initADC():
    global i2c
    global adc
    i2c = busio.I2C(board.SCL, board.SDA)
    adc = ADS.ADS1115(i2c)
    adc.gain = 8

def initComp():
    global compass
    compass = adafruit_mlx90393.MLX90393(i2c, gain=adafruit_mlx90393.GAIN_1X)

#checking status variables is databes and executing appropriate functions
def checkStatus():
    global lastCheck
    global isAuto
    if(time.time()-lastCheck>=1):
        lastCheck = time.time()
        status = api.getStatus()
        if status == False:
            return False
        else:
            if status['abort']==True:
                isAuto=False
                updateEngine({
                    'rightSpeed': 0,
                    'leftSpeed': 0
                })
                api.deletAllWaypoints()
            if status['automation']==True:
                isAuto=True
            if status['delMapData']==True:
                api.removeMapData()
            if status['delData']==True:
                api.removeData()
                api.deletAllWaypoints()
            api.clearStatus()

#wip
def initEngine():
    engineSpeed['left'] = 100
    engineSpeed['right'] = 100
    if engineSpeed['left']>=0:
        motorLeft.forward(mapVal(engineSpeed['left'],0,100,0.2,0.8))
    else:
        motorLeft.backward(mapVal(-1*engineSpeed['left'],0,100,0.2,0.8))

    if engineSpeed['right']>=0:
        motorRight.forward(mapVal(engineSpeed['right'],0,100,0.2,0.8))
    else:
        motorRight.backward(mapVal(-1*engineSpeed['right'],0,100,0.2,0.8))

    time.sleep(5)

    engineSpeed['left'] = 0
    engineSpeed['right'] = 0

    if engineSpeed['left']>=0:
        motorLeft.forward(mapVal(engineSpeed['left'],0,100,0.2,0.8))
    else:
        motorLeft.backward(mapVal(-1*engineSpeed['left'],0,100,0.2,0.8))

    if engineSpeed['right']>=0:
        motorRight.forward(mapVal(engineSpeed['right'],0,100,0.2,0.8))
    else:
        motorRight.backward(mapVal(-1*engineSpeed['right'],0,100,0.2,0.8))

    api.updateSpeed(engineSpeed)

#main loop function (automodeneed fix)
def start():
    global completedOneTrip
    global currentWaypoint
    while True:      
        checkStatus()

        if not isAuto:
            global lastEngineUpdate
            if(time.time()-lastEngineUpdate>=1):
                lastEngineUpdate=time.time()
                updateEngine(api.getSpeed())
        else:
            if completedOneTrip:
                currentWaypoint=api.getOneWaypoint()
                completedOneTrip=False
                temporatyVal= False
                newSpeedValueFromAuto = 0
                while not temporatyVal:
                    newSpeedValueFromAuto, temporatyVal = auto.start(currentWaypoint, getCompass(), getGPS()) #{'longitude': longitude, 'latitude': latitude}
                    print (newSpeedValueFromAuto)
                    updateEngine(newSpeedValueFromAuto)
            newSpeedValueFromAuto, completedOneTrip = auto.move(currentWaypoint, getCompass(), getGPS())
            print (newSpeedValueFromAuto)
            updateEngine(newSpeedValueFromAuto)
        
        sendData()
        
api.initSpeed()
initGPS()
initADC()
initThermSenor()
initComp()

initEngine()

start()


