import os
import requests, json
import time

active = True
art = '''_______________________   _________            _____             ______
___    |__  __ \___  _/   __  ____/______________  /________________  /
__  /| |_  /_/ /__  /     _  /    _  __ \_  __ \  __/_  ___/  __ \_  / 
_  ___ |  ____/__/ /      / /___  / /_/ /  / / / /_ _  /   / /_/ /  /  
/_/  |_/_/     /___/      \____/  \____//_/ /_/\__/ /_/    \____//_/   
                                                                       '''


dbIPwithPort = "192.168.179.125:3000"

r = requests.get('http://'+ dbIPwithPort +'/1')
#print(r)
data = r.json()
dataCharge = json.dumps(data)
automaticCharging = data['automaticCharging']

r = requests.get('http://'+ dbIPwithPort +'/2')
#print(r)
data = r.json()
dataCharge = json.dumps(data)
chargingAmp = data['chargingAmp']

print(art)

while active:
    print()
    print("1) Enable Automatic Charging")
    print("2) Disable Automatic Charging")
    print("0) Exit")
    print()

    try: 
        answer = input("Option: ")
        print()

        if answer == "1":
            print()
            print("Enabling Automatic Charging")
            time.sleep(1)
            print()
            print()
            os.system('curl -X POST -d "automaticCharging=1" http://'+ dbIPwithPort +'/1')
            print()
            print()
            time.sleep(2)
            os.system('cls')
            print(art)
        elif answer == "2":
            print()
            print("Disabling Automatic Charging")
            time.sleep(1)
            print()
            print()
            os.system('curl -X POST -d "automaticCharging=0" http://'+ dbIPwithPort +'/1')
            print()
            print()
            time.sleep(2)
            os.system('cls')
            print(art)
        elif answer == "0":
            active = False
            print()
        else: 
            print()
            print ("Please select a valid option number")
            print()
    except NameError:  
        print()
        print ("NameError: Please Use Numbers Only")
        print()
    except SyntaxError: 
        print()
        print ("SyntaxError: Please Use Numbers Only")
        print()
    except TypeError:  
        print()
        print ("TypeError: Please Use Numbers Only")
        print()
    except AttributeError:  
        print()
        print ("AttributeError: Please Use Numbers Only")
        print()