import serial
import os
import subprocess
import time
import signal
import sys
import time



#constants

DEBUG=True

WAIT_TIME_FOR_BLE = 10

ADDR='98:D3:32:21:9D:45'

rfcomm_sh=''

LIMIT=100

#variables

left_val=0
right_val=0

increment=10

last_ble_update=0

#bluetooth serial initialisation

def init_ble_serial(second_time=False):
    if not second_time:
        os.system("sudo echo Sudo access granted!")
    print("Connecting to control board")
    rfcomm_sh = subprocess.Popen(['sudo','rfcomm','connect','0','98:D3:32:21:9D:45'],stdout=subprocess.DEVNULL)
    time.sleep(WAIT_TIME_FOR_BLE)
    try: 
        global SERIAL_BLE
        SERIAL_BLE=serial.Serial('/dev/rfcomm0',baudrate=9600,timeout=100)
        #SERIAL_BLE.write(b"100;100")
    except:
        print("Device not available")
        while True:
            anwser=input("Try again? [y/N]: ")
            if anwser=="":
                sys.exit()
            elif anwser=='n' or anwser=='N' or anwser=='No' or anwser=='no' or anwser=='NO':
                sys.exit()
            elif anwser=='y' or anwser=='Y' or anwser=='Yes' or anwser=='yes' or anwser=='YES':
                init_ble_serial(second_time=True)
                break
            else:
                print("Wrong command")