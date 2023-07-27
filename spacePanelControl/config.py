#!/bin/python3
import uinput
import pygame
import enum 

IC0A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC0B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }  

IC1A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC1B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }                          

IC2A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC2B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }  

IC3A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC3B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }  

IC4A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC4B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }  

IC5A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC5B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }  

IC6A_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
                        }

IC6B_uinput_map = {     0: uinput.KEY_0,
                        1: uinput.KEY_0,
                        2: uinput.KEY_0,
                        3: uinput.KEY_0,
                        4: uinput.KEY_0,
                        5: uinput.KEY_0,
                        6: uinput.KEY_0,
                        7: uinput.KEY_0,
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


//Key to sound maps


IC0A_sound_map = {     
			0: "startupsequence.wav",
                        1: "startupsequence.wav",
                        2: "startupsequence.wav",
                        3: "startupsequence.wav",
                        4: "startupsequence.wav",
                        5: "startupsequence.wav",
                        6: "startupsequence.wav",
                        7: "startupsequence.wav",
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
