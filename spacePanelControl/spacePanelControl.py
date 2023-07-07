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

#enumeration definitions for each panel and button name in the spaceship
class TopPanel_IC0_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 
class TopPanel_IC0_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 

class TopPanel_IC1_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 
class TopPanel_IC1_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 

class TopPanel_IC2_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 
class TopPanel_IC2_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2     

class FrontSidePanel_IC3_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class FrontSidePanel_IC3_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   

class FrontSidePanel_IC4_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class FrontSidePanel_IC4_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   


class BackSidePanel_IC5_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class BackSidePanel_IC5_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   

class BackSidePanel_IC6_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class BackSidePanel_IC6_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   


#create dictionary to hold IO expander button definitions,  this is how the buttons are physically configured in the spaceship
button_definitions = {  '0A':TopPanel_IC0_A,
                        'TOPPANEL_IC0_PORTA':TopPanel_IC0_A,
                        '0B':TopPanel_IC0_B,
                        'TOPPANEL_IC0_PORTB':TopPanel_IC0_B,
                        '1A':TopPanel_IC1_A,
                        'TOPPANEL_IC1_PORTA':TopPanel_IC1_A,
                        '1B':TopPanel_IC1_B,
                        'TOPPANEL_IC1_PORTB':TopPanel_IC1_B,
                        '2A':TopPanel_IC2_A,
                        'TOPPANEL_IC2_PORTA':TopPanel_IC2_A,
                        '2B':TopPanel_IC2_B,
                        'TOPPANEL_IC2_PORTB':TopPanel_IC2_B,

                        '3A':FrontSidePanel_IC3_A,
                        'FRONTSIDEPANEL_IC3_PORTA':FrontSidePanel_IC3_A,
                        '3B':FrontSidePanel_IC3_B,
                        'FRONTSIDEPANEL_IC3_PORTB':FrontSidePanel_IC3_B,
                        '4A':FrontSidePanel_IC4_A,
                        'FRONTSIDEPANEL_IC4_PORTA':FrontSidePanel_IC4_A,
                        '4B':FrontSidePanel_IC4_B,
                        'FRONTSIDEPANEL_IC4_PORTB':FrontSidePanel_IC4_B,

                        '5A':BackSidePanel_IC5_A,
                        'BACKSIDEPANEL_IC5_PORTA':BackSidePanel_IC5_A,
                        '5B':BackSidePanel_IC5_B,
                        'BACKSIDEPANEL_IC5_PORTB':BackSidePanel_IC5_B,
                        '6A':BackSidePanel_IC6_A,
                        'BACKSIDEPANEL_IC6_PORTA':BackSidePanel_IC6_A,
                        '6B':BackSidePanel_IC6_B,
                        'BACKSIDEPANEL_IC6_PORTB':BackSidePanel_IC6_B
                        }

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

        #request from serial device status of all buttons
        foundPort.write("GSTAT".encode('utf-8'))

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

                #parse execution command and process changes in state by playing sounds or sending keypresses 
                print("run: " + updateMessage)
                chipNumber = int(updateMessage[0][0])
                portLetter = updateMessage[0][1]
                portStatus = updateMessage[1]
                #print("chip number: " + str(chipNumber))
                if chipNumber >= 0 and chipNumber <= 2: 
                    #parse Top Panel buttons
                    print("Parsing Top Panel Buttons\n")

                    if portLetter == 'A':
                        print(portLetter)

                    else:
                        print(portLetter)

                    device.emit_click(uinput.KEY_HOME)
                elif chipNumber >= 3 and chipNumber <= 4:
                    #parse Front Side Panel buttons
                    print("Parsing Front Side Panel Buttons\n")
                elif chipNumber >= 5 and chipNumber <= 6:
                    #parse Back Side Panel buttons
                    print("Parsing Back Side Panel Buttons\n")
                    device.emit_click(uinput.KEY_B)
                else:
                    #invalid input
                    print("ERROR: Invalid chip number\n")

                #process changes in state by playing sounds or espeaking
              
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


