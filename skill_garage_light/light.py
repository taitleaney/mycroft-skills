#!/usr/bin/env python
# coding=utf-8
import sys
from time import sleep

from lifxlan import LifxLAN


def main():
	
    # instantiate LifxLAN client, num_lights may be None (unknown).
    # In fact, you don't need to provide LifxLAN with the number of bulbs at all.
    # lifx = LifxLAN() works just as well. Knowing the number of bulbs in advance 
    # simply makes initial bulb discovery faster.
	
	lifx = LifxLAN()
	
    # get devices
	devices = lifx.get_lights()
	bulb = devices[0]
    
    # get original state
	original_power = bulb.get_power()
            
	if original_power == 0:
		bulb.set_power("on")
		
	else:
		bulb.set_power("off")

if __name__=="__main__":
	main()
