import requests, json
from timeloop import Timeloop
from datetime import timedelta
from wallbox import Wallbox, Statuses
import logging
import time
import datetime

wallboxEmail = ""
wallboxPassword = ""
sonnenBatterieIP = ""
dataBaseIPwithPort = ""
dataCharge = ""
dataBattery = ""
wallboxID = ""
tl = Timeloop()
percentage = ""
automaticCharging = ""
chargingAmp = ""
lastSent = -1
full = False
currentlyCharging = "Start"
pausedByAPI = False



def configRead():
    global wallboxEmail, wallboxPassword, sonnenBatterieIP, dataBaseIPwithPort, wallboxID
    filename = "settings.config"
    contents = open(filename).read()
    config = eval(contents)
    wallboxEmail = config['wallboxEmail']
    wallboxPassword = config['wallboxPassword']
    sonnenBatterieIP = config['sonnenBatterieIP']
    dataBaseIPwithPort = config['dataBaseIPwithPort']
    wallboxID = config['wallboxID']

def getDataCharge():
    global chargingAmp, automaticCharging, dataCharge
    r = requests.get('http://'+ dataBaseIPwithPort +'/1')
    #print(r)
    data = r.json()
    dataCharge = json.dumps(data)
    automaticCharging = data['automaticCharging']

def getDataAmp():
    global chargingAmp, automaticCharging, dataCharge
    r = requests.get('http://'+ dataBaseIPwithPort +'/2')
    #print(r)
    data = r.json()
    dataCharge = json.dumps(data)
    chargingAmp = data['chargingAmp']

def getDataBattery():
    global percentage, dataBattery
    r = requests.get('http://'+ sonnenBatterieIP +'/api/v2/status')
    #print(r)
    data = r.json()
    dataBattery = json.dumps(data)
    #print(dataBattery)
    percentage = data['RSOC']

@tl.job(interval=timedelta(seconds=300))
def checkAndCommand():
    global percentage, automaticCharging, chargingAmp, wallbox, lastSent, full, currentlyCharging

    getDataCharge()
    getDataBattery()
    getDataAmp()

    print("-----------------------")
    print("Battery percentage: " + str(percentage))
    print("Automatic Charging: " + str(automaticCharging))
    print("Charging Amp: " + str(chargingAmp))

    # Wallbox

    try:
        if percentage >= 80:
            if automaticCharging == "1":
                print("Resume Charging")
                wallbox.resumeChargingSession(wallboxID)
                pausedByAPI = False
            elif automaticCharging == "0" and pausedByAPI == False:
                print("Stop Charging")
                wallbox.resumeChargingSession(wallboxID)
                pausedByAPI = True
        elif percentage <= 75:
            print("Stop Charging")
            wallbox.pauseChargingSession(wallboxID)
            pausedByAPI = False
    except:
        print("Exception")
        logging.exception("Error message ")


configRead()
wallbox = Wallbox(wallboxEmail, wallboxPassword)
wallbox.authenticate()  

if __name__ == "__main__":
    tl.start(block=True)