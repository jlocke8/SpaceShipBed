#!/bin/python3
from ast import Pass
import uinput       #used to programmatically send keyboard,mouse, or joystick inputs
import pygame       #used in this program to manipulate sounds 
import serial       #used to control access to serial ports
import serial.tools.list_ports  #used to find a list of serial ports
import time         #used to control delays 
import subprocess   #used to make system command line calls
import enum         #used to make enumerations 

import config       #external python file which holds configuration dictionaries specific to this spaceship program (button mapping to sounds and keypresses, etc)

#setup variable to hold switch status data
status_top_panel = list()
status_backside_panel = list()
status_frontside_panel = list()
button_status = [[hex(0x00) for x in range(2)] for y in range(8)]   #initialize 8x2 two dimensional array
execute_list = list()


#create a list of all the uinput key definitions created from the config library to be defined as a uinput device
uinputlist = []
for key in config.button_uinput_map:    #get each top level key in dictionary
    for subkey in config.button_uinput_map[key]:    #for each top level key, enter toplevel key and get every subkey
        uinputlist.append(config.button_uinput_map[key][subkey])  #get each item in nested dictionary
print(uinputlist)

#configure uinput virtual keyboard using the uinput key definitions
device = uinput.Device(
        uinputlist
#        uinput.KEY_A,
#        uinput.KEY_B,
#        uinput.KEY_C,            
        )

device_mouse = uinput.Device([
                uinput.BTN_LEFT,
                uinput.BTN_RIGHT,
                uinput.REL_X,
                uinput.REL_Y,
                ])

time.sleep(1)

##with uinput.Device(events) as device:
'''
for i in range(10):
    device.emit_click(uinput.KEY_B)
'''

for i in range(20):
    device_mouse.emit(uinput.REL_X, 5)
    device_mouse.emit(uinput.REL_Y, 5)

time.sleep(1)

for i in range(20):
    device_mouse.emit(uinput.REL_X, -5)
    device_mouse.emit(uinput.REL_Y, -5)


class statusMessage:
    chipNumber=""
    chipNumStr=""
    portLetter=""
    portStatus=""


#main program
def main():
    #initialize sound
    pygame.mixer.init(44100, -16,2,1024)

    #subprocess.run("espeak -v en-n 'start up sequence initialized...' -p 0 -a 200 -s 150", shell=True)
    pygame.mixer.Sound("./sounds/startupsequence.wav").play()

    print('\nbutton definitions dictionary:\n' + str(config.button_definitions) + '\n')

    #configure and open correct serial connection
    foundPort = scanConnections()

    if foundPort is None:
        print("ERROR! No valid serial connection found")
    else:
        print("Success. Connection established to port: " + str(foundPort.port))

        time.sleep(1)
        #request from serial device status of all buttons        
        print(foundPort)
        serialCommand= "GSTAT"  
        #send command message to serial device
        for i in serialCommand:
            foundPort.write(i.encode())     #need to encode string to utf-8 (bytes)
            time.sleep(0.001)   #need to add small delay for timing purposes, otherwise serial gets scrambled message
        #time.sleep(1)

        #constantly listen for serial data and execute updates
        try: 
            print("Ctrl-C to end")    
            status = 0        



            # while(timeOut is False):    #only poll for status without execution for a fixed time
            #     status = pollSerialLoop(foundPort, True)    #scan status messages but ignore execution
            #     timeOutCount = time.perf_counter()
            #     if (timeOutCount - timeOutStart) >= 2:
            #         timeOut = True            
                    

            while(status == 0):
                #for a period of time, read in the status of all buttons as a result of sending "GSTAT" command to update button status banks
                timeOutStart = time.perf_counter()
                timeOut = False
                if timeOut == False:
                    status= pollSerialLoop(foundPort,True)
                    timeOutCount = time.perf_counter()
                    if (timeOutCount - timeOutStart) >= 2:
                        timeOut = True
                else:
                    #poll status and add updates the execution queue
                    status = pollSerialLoop(foundPort, False)   #scan status messages and queue to execute

                #execute changes from execute_list
                status = executeChanges()

        except KeyboardInterrupt as e:
            print("Serial Polling Stopped\n\n")
            raise


#scan through serial connections and test which one is correct
def scanConnections():

    #get list of serial com ports
    comListRaw = serial.tools.list_ports.comports()
    availPorts = []
    for comport in comListRaw:
        availPorts.append(comport.device)
    print("ports found: ")
    print(availPorts)

    #look for serial heartbeat message 
    heartBeatMessage = "(^_^)\n"  #this is the message that is searched for in a valid serial connection
    connection = None   
    for each in availPorts:
        #print(each)
        testConnect = serial.Serial(each, 230400, timeout=0.03)
        timeOutStart = time.perf_counter()
        timeOut = False
        while(timeOut is False):
            timeOutCount = time.perf_counter()
            #print(int(timeOutCount- timeOutStart), end='')
            testRead = testConnect.readline().decode('utf-8')        
            print(testRead) if testRead is not "" else None

            if testRead == "(^_^)\n":
                connection = testConnect
                #subprocess.run("espeak -v zh-yue 'serial connection established...' -p 0 -a 200 -s 150", shell=True)
                pygame.mixer.Sound("./sounds/serialconnectionest.wav").play()
                break        
            if (timeOutCount - timeOutStart) >= 5:
                timeOut = True            
                print("Connection timed out to port: " + str(each))

    return connection


#read from serial connection and update informtion
def pollSerialLoop(connection, ignoreExecute):

    readSerial = connection.readline().decode('utf-8') 
    if len(readSerial) > 0:
        print(readSerial)

        #parse data to see what buttons are updating, remove white space
        if '#' in readSerial:
            parsedMessages = [x for x in readSerial.replace('\n','').replace('\r','').split("#") if x]
            #print(parsedMessages)

            #update the status banks with given information              
            for eachMsg in parsedMessages:
                msg = decodeMessage(eachMsg)
                if msg.portLetter == 'A':
                    button_status[int(msg.chipNumStr[0])][0] = hex(msg.portStatus)
                else: 
                    button_status[int(msg.chipNumStr[0])][1] = hex(msg.portStatus)
            print("bStatus:" + str(button_status))    

            #add updates to execution queue
            if ignoreExecute is False:
                execute_list.extend(parsedMessages)
                print("exeList:" + str(execute_list))

    return 0






def executeChanges():             
    #for each in execute_list:
        if len(execute_list) >= 1:
            updateMessage = execute_list.pop().split(":")
            if len(updateMessage) == 2:

                #parse execution command and process changes in state by playing sounds or sending keypresses 
                print("run: " + str(updateMessage))
                msg = decodeMessage(updateMessage)
                chipNumber = int(updateMessage[0][0])
                chipNumStr = updateMessage[0]
                portLetter = updateMessage[0][1]
                portStatus = int(updateMessage[1], 16)    #convert string to hex number
                #print("chip number: " + str(chipNumber))

                for bitshift in range(0, 8):
                    if(msg.portStatus & (1<<bitshift)):
                        print(msg.chipNumStr)
                        print(config.button_uinput_map[msg.chipNumStr][bitshift])
                        device.emit_click(config.button_uinput_map[msg.chipNumStr][bitshift])
                        print(config.button_sound_map[msg.chipNumStr][bitshift])
                        pygame.mixer.Sound(config.button_sound_map[msg.chipNumStr][bitshift]).play()
                if msg.chipNumber >= 0 and msg.chipNumber <= 2: 
                    #parse Top Panel buttons
                    print("Parsing Top Panel Buttons\n")

                    if msg.chipNumber == 0:
                        print(msg.chipNumber)

                        if msg.portLetter == 'A':
                            print(msg.portLetter)
                        else:
                            print(msg.portLetter)

                    if msg.chipNumber == 1:
                        print(msg.chipNumber)

                        if msg.portLetter == 'A':
                            print(msg.portLetter)
                        else:
                            print(msg.portLetter)

                    if msg.chipNumber == 2:
                        print(msg.chipNumber)

                        if msg.portLetter == 'A':
                            if msg.portStatus & (1<<0):
                                print(config.button_uinput_map['2A'][0])
                                device.emit_click(config.button_uinput_map['2A'][0])                              
                            if msg.portStatus & (1<<1):    
                                device.emit_click(uinput.KEY_B)  
                            if msg.portStatus & (1<<2):
                                device.emit_click(uinput.KEY_C)                              
                            if msg.portStatus & (1<<3):
                                device.emit_click(uinput.KEY_D)                              
                            if msg.portStatus & (1<<4):
                                device.emit_click(uinput.KEY_E)                              
                            if msg.portStatus & (1<<5):
                                device.emit_click(uinput.KEY_F)                              
                            if msg.portStatus & (1<<6):
                                device.emit_click(uinput.KEY_G)                              
                            if msg.portStatus & (1<<7):
                                device.emit_click(uinput.KEY_H)                              


                        else:
                            print(msg.portLetter)


                    device.emit_click(uinput.KEY_HOME)
                elif msg.chipNumber >= 3 and msg.chipNumber <= 4:
                    #parse Front Side Panel buttons
                    print("Parsing Front Side Panel Buttons\n")
                elif msg.chipNumber >= 5 and msg.chipNumber <= 6:
                    #parse Back Side Panel buttons
                    print("Parsing Back Side Panel Buttons\n")
                    device.emit_click(uinput.KEY_B)
                else:
                    #invalid input
                    print("ERROR: Invalid chip number\n")

                #process changes in state by playing sounds or espeaking
              
                #pygame.mixer.Sound("gauss.wav").play()

            else:
                print("ERROR! Invalid update message: " + str(updateMessage))

            #espeak -v en-n+f4 'poo poo jew...  activated...' -p 1000 -a 200 -s 200
            #espeak -v zh-yue+f4 'poo poo jew...  activated...' -p 1000 -a 200 -s 200
            #espeak -v vi 'blah connection established...' -p 10 -a 200 -s 150 -g 5
        
        return 0
    #pass




#this function takes the parsed serial message which looks like 0A:XX and interprets the meaning 
#the first two characters are the chip number and port letter respectively
#the message after ":" is a hex value of the port status
def decodeMessage(parsedMessage):
    splitMessage=parsedMessage.split(":")
    if len(splitMessage) == 2:          
        decoded = statusMessage()
        decoded.chipNumber = int(splitMessage[0][0])
        decoded.chipNumStr = splitMessage[0]    #this is a string
        decoded.portLetter = splitMessage[0][1]
        decoded.portStatus = int(splitMessage[1], 16)    #convert string to hex number
        return decoded
    else:
        return 1    #1 means error
    




if __name__=="__main__":
    print("This file is being ran directly")
    main()
else:
    print("This file is being imported")