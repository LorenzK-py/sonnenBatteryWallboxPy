# Automatic Car Charging Using Sonnen Batterie and Wallbox

This is a python project and database which will help you charge your Electric Vehicle easier and with less user input.

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

#Stop the database 
screen -r automaticCharging
#CTRL + C
```