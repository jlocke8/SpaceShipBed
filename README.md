# SpaceShipBed
This repo contains all the code for a bed turned spaceship.  There are two sides of the code:
1. Firmware that is programmed into an Arduino which reads status from all the spaceship buttons via GPIO expanders and then sends the status through a serial port via USB.
2. Python code to manage and act upon serial port button messages from a bunkbed turned spaceship.  This code turns into actionable items such as play a sound, turn on a light, or send a keystroke to interact with a game. 
