#!/bin/python3
from ast import Pass
import uinput       #used to programmatically send keyboard,mouse, or joystick inputs
import pygame       #used in this program to manipulate sounds 
import serial       #used to control access to serial ports
import serial.tools.list_ports  #used to find a list of serial ports
import time         #used to control delays 
import subprocess   #used to make system command line calls
import enum         #used to make enumerations 

#setup variable to hold switch status data
status_top_panel = list()
status_backside_panel = list()
status_frontside_panel = list()
button_status = [[hex(0x00) for x in range(8)] for y in range(2)]   #initialize 8x2 two dimensional array
execute_list = list()


class TopPanelSwitches_IC1_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 

#create dictionary to hold IO expander button definitions
button_definitions = {  '0A':TopPanelSwitches_IC1_A,
                        'TOPPANEL_IC1_PORTA':TopPanelSwitches_IC1_A,
                        '0B':{},
                        '1A':{},
                        '1B':{},
                        '2A':{},
                        '2B':{},
                        '3A':{},
                        '3B':{},
                        '4A':{},
                        '4B':{},
                        '5A':{},
                        '5B':{},
                        '6A':{},
                        '6B':{},
                        '7A':{},
                        '7B':{}    }

#configure uinput virtual keyboard
device = uinput.Device([
        uinput.KEY_A,
        uinput.KEY_B,
        uinput.KEY_C,
        ])

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

#print('hello')


#main program
def main():
    #initialize sound
    pygame.mixer.init(44100, -16,2,1024)

    #subprocess.run("espeak -v en-n 'start up sequence initialized...' -p 0 -a 200 -s 150", shell=True)
    pygame.mixer.Sound("startupsequence.wav").play()

    print('\nbutton definitions dictionary:\n' + str(button_definitions) + '\n')

    #configure and open correct serial connection
    foundPort = scanConnections()

    if foundPort is None:
        print("ERROR! No valid serial connection found")
    else:
        print("Success. Connection established to port: " + str(foundPort.port))

        #constantly listen for serial data and execute updates
        try: 
            print("Ctrl-C to end")    
            status = 0        
            while(status == 0):
                #poll status
                status = pollSerialLoop(foundPort)

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
                pygame.mixer.Sound("serialconnectionest.wav").play()
                break        
            if (timeOutCount - timeOutStart) >= 5:
                timeOut = True            
                print("Connection timed out to port: " + str(each))

    return connection


#read from serial connection and update informtion
def pollSerialLoop(connection):

    readSerial = connection.readline().decode('utf-8') 
    if len(readSerial) > 0:
        print(readSerial)

        #parse data to see what buttons are updating, remove white space
        if '#' in readSerial:
            parsedMessages = [x for x in readSerial.replace('\n','').replace('\r','').split("#") if x]
            #print(parsedMessages)

            #update the status banks with given information
            print("bStatus:" + str(button_status))       

            #add updates to execution queue
            execute_list.extend(parsedMessages)
            print("exeList:" + str(execute_list))

    return 0






def executeChanges():             
    #for each in execute_list:
        if len(execute_list) >= 1:
            updateMessage = execute_list.pop().split(":")
            if len(updateMessage) == 2:
                #process changes in state by playing sounds or espeaking
                print("run:" + str(updateMessage))               
                pygame.mixer.Sound("gauss.wav").play()

            else:
                print("ERROR! Invalid update message: " + str(updateMessage))

            #espeak -v en-n+f4 'poo poo jew...  activated...' -p 1000 -a 200 -s 200
            #espeak -v zh-yue+f4 'poo poo jew...  activated...' -p 1000 -a 200 -s 200
            #espeak -v vi 'blah connection established...' -p 10 -a 200 -s 150 -g 5
        
        return 0
    #pass


if __name__=="__main__":
    print("This file is being ran directly")
    main()
else:
    print("This file is being imported")
