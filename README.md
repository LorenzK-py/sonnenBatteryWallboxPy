# Automatic Car Charging Using Sonnen Batterie and Wallbox

This is a python project and database which will help you charge your Electric Vehicle easier and with less user input.

![Preview](preview.png?raw=true "Preview")

## Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Host the db.json on a Linux server by editing the start.sh file and launching using:

```bash
./start.sh
```
You can also use Screen to leave the database running without any windows open:

```bash
#Start the database
screen -S db ./start.sh

#Stop the database 
screen -r db
#CTRL + C
```
Now you can start the main Python program on a server:
```bash
python3 main.py
```
or alternatively using Screen:
```bash
screen -S automaticCharging python3 main.py

#Stop the program
screen -r automaticCharging
#CTRL + C
```
## Controlling the API
You can control the API using the apiControl.py file (You may also want to convert the file to .exe to use it on any pc)

```bash
_______________________   _________            _____             ______
___    |__  __ \___  _/   __  ____/______________  /________________  /
__  /| |_  /_/ /__  /     _  /    _  __ \_  __ \  __/_  ___/  __ \_  /
_  ___ |  ____/__/ /      / /___  / /_/ /  / / / /_ _  /   / /_/ /  /
/_/  |_/_/     /___/      \____/  \____//_/ /_/\__/ /_/    \____//_/


1) Enable Automatic Charging
2) Disable Automatic Charging
0) Exit

Option:
```