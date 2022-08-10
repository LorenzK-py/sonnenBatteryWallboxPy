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
Your car will now start and stop charging according to the values set in settings.config. (When plugging in your vehicle you need to unlock it in the Wallbox app first)

## Controlling the API
You can control the API using the apiControl.py file (You need to edit the IP in the file first + you may also want to convert the file to .exe to use it on any pc)
