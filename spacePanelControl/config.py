#!/bin/python3
import uinput
import pygame
import enum 

#TOP PANEL
IC0A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},    #polarity 1 means button is actuated when signal high, polarity 0, is button is actuated when signal is low
                        1: {"polarity": 1, "key": uinput.KEY_0},    #some buttons require a specific polarity setting to actuate when pressed as opposed to actuate when released
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC0B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }  
#TOP PANEL
IC1A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC1B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC2A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC2B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }  
#FRONT SIDE PANEL
IC3A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#FRONT SIDE PANEL
IC3B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }  
#FRONT SIDE PANEL
IC4A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#FRONT SIDE PANEL
IC4B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL
IC5A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 0, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL2
IC5B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_1},
                        7: {"polarity": 0, "key": uinput.KEY_2}
                    }
#BACK SIDE PANEL
IC6A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL
IC6B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }

#create dictionary to hold uinput mappings
button_uinput_map = {   
			            '0A':IC0A_uinput_map,
                        '0B':IC0B_uinput_map,
                        '1A':IC1A_uinput_map, 
                        '1B':IC1B_uinput_map,
                        '2A':IC2A_uinput_map,
                        '2B':IC2B_uinput_map,
                        '3A':IC3A_uinput_map,
                        '3B':IC3B_uinput_map,
                        '4A':IC4A_uinput_map,
                        '4B':IC4B_uinput_map,
                        '5A':IC5A_uinput_map,
                        '5B':IC5B_uinput_map,
                        '6A':IC6A_uinput_map,
                        '6B':IC6B_uinput_map,
                    }


#Key to sound maps

IC0A_sound_map = {     
			            0: { #Port's Position Number
                            0: "",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: ""   #"On" state
                        },
                        1: {
                            0: "",
                            1: "./sounds/nuke.wav"
                        },
                        2:{
                            0: "",
                            1: "./sounds/plasmabomb.wav"
                        },
                        3:{
                            0: "",
                            1: "./sounds/pulselaser.wav"
                        },
                        4:{
                            0: "",
                            1: "./sounds/deathray.wav"
                        },
                        5:{
                            0: "",
                            1: "./sounds/hyperdisintegratorcannon.wav"
                        },
                        6:{
                            0: "",
                            1: "./sounds/gausscannon.wav"
                        },
                        7:{
                            0: "",
                            1: "./sounds/autocannon.wav"
                        }
                    }  

IC0B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/apu1Off.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/apu1On.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/",
                            1: "./sounds/turbine.mp3"
                        },
                        2:{
                            0: "./sounds/",
                            1: "./sounds/f16-fighter-jet-start.mp3"
                        },
                        3:{
                            0: "./sounds/fuelpump1Off.wav",
                            1: "./sounds/fuelpump1On.wav"
                        },
                        4:{
                            0: "",
                            1: ""
                        },
                        5:{
                            0: "./sounds/jettison.wav",
                            1: ""
                        },
                        6:{
                            0: "./sounds/cruisemissile.wav",
                            1: ""
                        },
                        7:{
                            0: "./sounds/torpedo.wav",
                            1: ""
                        }
                    }  

IC1A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/firepowerOff.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/firepowerOn.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/lightbulbpowerOff.wav",
                            1: "./sounds/lightbulbpowerOn.wav"
                        },
                        2:{
                            0: "./sounds/littlepigpowerOff.wav",
                            1: "./sounds/littlepigpowerOn.wav"
                        },
                        3:{
                            0: "./sounds/treepowerOff.wav",
                            1: "./sounds/treepowerOn.wav"
                        },
                        4:{
                            0: "./sounds/monsterpowerOff.wav",
                            1: "./sounds/monsterpowerOn.wav"
                        },
                        5:{
                            0: "./sounds/totoropowerOff.wav",
                            1: "./sounds/totoropowerOn.wav"
                        },
                        6:{
                            0: "./sounds/autotargetOff.wav",
                            1: "./sounds/autotargetOn.wav"
                        },
                        7:{
                            0: "./sounds/toepowerOff.wav",
                            1: "./sounds/toepowerOn.wav"
                        }
                    }  

IC1B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/thrusters1Off.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/thrusters1On.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/mainengine1Off.wav",
                            1: "./sounds/mainengine1On.wav"
                        },
                        2:{
                            0: "./sounds/mainengine2Off.wav",
                            1: "./sounds/mainengine2On.wav"
                        },
                        3:{
                            0: "./sounds/thrusters2Off.wav",
                            1: "./sounds/thrusters2On.wav"
                        },
                        4:{
                            0: "./sounds/retrorocket1On.wav",
                            1: "./sounds/retrorocket1Off.wav"
                        },
                        5:{
                            0: "./sounds/retrorocket2On.wav",
                            1: "./sounds/retrorocket2Off.wav"
                        },
                        6:{
                            0: "./sounds/stabilizer1On.wav",
                            1: "./sounds/stabilizer1Off.wav"
                        },
                        7:{
                            0: "./sounds/stabilizer2On.wav",
                            1: "./sounds/stabilizer2Off.wav"
                        }
                    }  

IC2A_sound_map = {     
			            0: { #Port's Position Number
                            0: "",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: ""   #"On" state
                        },
                        1: {
                            0: "",
                            1: "./sounds/toes.wav"
                        },
                        2:{
                            0: "./sounds/veganfart.mp3",
                            1: "./sounds/atootieOn.wav"
                        },
                        3:{
                            0: "./sounds/wetfart.mp3",
                            1: "./sounds/buttcrack.wav"
                        },
                        4:{
                            0: "./sounds/steam-release.mp3",
                            1: "./sounds/driedpee.wav"
                        },
                        5:{
                            0: "./sounds/chargefart.mp3",
                            1: "./sounds/poop.wav"
                        },
                        6:{
                            0: "",
                            1: "./sounds/footface.wav"
                        },
                        7:{
                            0: "./sounds/fart_echo.mp3",
                            1: "./sounds/dabadu.wav"
                        }
                    }  

IC2B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/apu2Off.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/apu2On.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/",
                            1: "./sounds/turbine.mp3"
                        },
                        2:{
                            0: "./sounds/",
                            1: "./sounds/f16-fighter-jet-start.mp3"
                        },
                        3:{
                            0: "./sounds/fuelpump2Off.wav",
                            1: "./sounds/fuelpump2On.wav"
                        },
                        4:{
                            0: "./sounds/",
                            1: "./sounds/circulate.mp3"
                        },
                        5:{
                            0: "./sounds/",
                            1: "./sounds/distress-signal-3.mp3"
                        },
                        6:{
                            0: "./sounds/",
                            1: "./sounds/distress-signal.mp3"
                        },
                        7:{
                            0: "./sounds/",
                            1: "./sounds/distress-signal-2.mp3"
                        }
                    }  

IC3A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/extlightsOff.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/extlightsOn.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/heaterOff.wav",
                            1: "./sounds/heaterOn.wav"
                        },
                        2:{
                            0: "./sounds/airconOff.wav",
                            1: "./sounds/airconOn.wav"
                        },
                        3:{
                            0: "./sounds/filterOff.wav",
                            1: "./sounds/filterOn.wav"
                        },
                        4:{
                            0: "./sounds/cloakOff.wav",
                            1: "./sounds/cloakOn.wav"
                        },
                        5:{
                            0: "./sounds/targetingOff.wav",
                            1: "./sounds/targetingOn.wav"
                        },
                        6:{
                            0: "./sounds/jammerOff.wav",
                            1: "./sounds/jammerOn.wav"
                        },
                        7:{
                            0: "./sounds/proximityOff.wav",
                            1: "./sounds/proximityOn.wav"
                        }
                        
                    }  

IC3B_sound_map = {                        
                        0: { #Port's Position Number
                            0: "./sounds/radarOff.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/radarOn.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/beaconOff.wav",
                            1: "./sounds/beaconOn.wav"
                        },
                        2:{
                            0: "./sounds/gyroscopeOff.wav",
                            1: "./sounds/gyroscopeOn.wav"
                        },
                        3:{
                            0: "./sounds/radioOff.wav",
                            1: "./sounds/radioOn.wav"
                        },
                        4:{
                            0: "./sounds/microphoneOff.wav",
                            1: "./sounds/microphoneOn.wav"
                        },
                        5:{
                            0: "./sounds/autopilotOff.wav",
                            1: "./sounds/autopilotOn.wav"
                        },
                        6:{
                            0: "./sounds/lapoopooOff.wav",
                            1: "./sounds/lapoopooOn.wav"
                        },
                        7:{
                            0: "./sounds/transceiverOff.wav",
                            1: "./sounds/transceiverOn.wav"
                        }
                    }  

IC4A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/phasedarray1Off.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/phasedarray1On.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/phasedarray2Off.wav",
                            1: "./sounds/phasedarray2On.wav"
                        },
                        2:{
                            0: "./sounds/comlink1Off.wav",
                            1: "./sounds/comlink1On.wav"
                        },
                        3:{
                            0: "./sounds/comlink2Off.wav",
                            1: "./sounds/comlink2On.wav"
                        },
                        4:{
                            0: "./sounds/forwardshieldsOff.wav",
                            1: "./sounds/forwardshieldsOn.wav"
                        },
                        5:{
                            0: "./sounds/aftshieldsOff.wav",
                            1: "./sounds/aftshieldsOn.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC4B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC5A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/lifesupportOff.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/lifesupportOn.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/powerbankOff.wav",
                            1: "./sounds/powerbankOn.wav"
                        },
                        2:{
                            0: "./sounds/booboojuiceOff.wav",
                            1: "./sounds/booboojuiceOn.wav"
                        },
                        3:{
                            0: "./sounds/cellsmainOn.wav",
                            1: "./sounds/cellsmainOff.wav"
                        },
                        4:{
                            0: "./sounds/cellsauxOn.wav",
                            1: "./sounds/cellsauxOff.wav"
                        },
                        5:{
                            0: "./sounds/atootieOn.wav",
                            1: "./sounds/atootieOff.wav"
                        },
                        6:{
                            0: "./sounds/footytoeOn.wav",
                            1: "./sounds/footytoeOff.wav"
                        },
                        7:{
                            0: "./sounds/",
                            1: "./sounds/"
                        }
                    }  

IC5B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/reactor1Off.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/reactor1On.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/pump1Off.wav",
                            1: "./sounds/pump1On.wav"
                        },
                        2:{
                            0: "./sounds/generator1Off.wav",
                            1: "./sounds/generator1On.wav"
                        },
                        3:{
                            0: "./sounds/reactor2Off.wav",
                            1: "./sounds/reactor2On.wav"
                        },
                        4:{
                            0: "./sounds/pump2Off.wav",
                            1: "./sounds/pump2On.wav"
                        },
                        5:{
                            0: "./sounds/generator2Off.wav",
                            1: "./sounds/generator2On.wav"
                        },
                        6:{
                            0: "./sounds/o2synthOn.wav",
                            1: "./sounds/o2synthOff.wav"
                        },
                        7:{
                            0: "./sounds/co2scrubberOn.wav",
                            1: "./sounds/co2scrubberOff.wav"
                        }
                    }  

IC6A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC6B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/"   #"On" state
                        },
                        1: {
                            0: "./sounds/",
                            1: "./sounds/"
                        },
                        2:{
                            0: "./sounds/",
                            1: "./sounds/sonarping.mp3"
                        },
                        3:{
                            0: "./sounds/",
                            1: "./sounds/sonarsweepbeep.mp3"
                        },
                        4:{
                            0: "./sounds/",
                            1: "./sounds/"
                        },
                        5:{
                            0: "./sounds/",
                            1: "./sounds/"
                        },
                        6:{
                            0: "./sounds/",
                            1: "./sounds/"
                        },
                        7:{
                            0: "./sounds/",
                            1: "./sounds/"
                        }
                    }  

#create dictionary to hold sound mappings
button_sound_map = {   
			            '0A':IC0A_sound_map,
                        '0B':IC0B_sound_map,
                        '1A':IC1A_sound_map, 
                        '1B':IC1B_sound_map,
                        '2A':IC2A_sound_map,
                        '2B':IC2B_sound_map,
                        '3A':IC3A_sound_map,
                        '3B':IC3B_sound_map,
                        '4A':IC4A_sound_map,
                        '4B':IC4B_sound_map,
                        '5A':IC5A_sound_map,
                        '5B':IC5B_sound_map,
                        '6A':IC6A_sound_map,
                        '6B':IC6B_sound_map,
                    }










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
    A0_IC2_Launch2=0 
    A1_IC2_Toes=1
    A2_IC2_Atootie=2
    A3_IC2_ButtCrack=3
    A4_IC2_DriedPee=4
    A5_IC2_Poop=5
    A6_IC2_FootFace=6
    A7_IC2_Dabadu=7
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

                      