'''
-------------------------------------------------------------------------------
Name:		microbit_logic_assignment.py
Purpose:	The program is a plant monitoring device that
            allows you to find out whether your plant is in
            perfect condition. For example if the moisture level
            is too low. the device will notify you. >

Author:	Zhou.Di, Dehghani Emad

Created:	30/10/2019
------------------------------------------------------------------------------
'''

from microbit import *
import music

# Assign pins

sound = pin0
moisture_sensor = pin1
led_red = pin2
led_green = pin16

while True:
    # sensor temperature
    if button_a.is_pressed():
        # check if temperature is equal to 30 degrees celsius
        if temperature() == 30:
            led_green.write_digital(1)
            led_red.write_digital(0)
            display.scroll("The temperature is perfect!")
            music.play(music.NYAN)
        elif temperature() > 30:
            led_red.write_digital(1)
            led_green.write_digital(0)
            display.scroll("Put your plant somewhere cooler!!")
            music.play(music.DADADADUM)
        else:
            led_red.write_digital(1)
            led_green.write_digital(0)
            music.play(music.DADADADUM)
            display.scroll("Put your plant somewhere hotter!!")
    elif button_b.is_pressed():
        # check if the moisture level is equal to 50.
        if (moisture_sensor.read_analog() < 500):
            led_green.write_digital(0)
            led_red.write_digital(1)
            display.scroll("Water your plant more!!")
            music.play(music.DADADADUM)
        elif (moisture_sensor.read_analog() > 510):
            led_green.write_digital(0)
            led_red.write_digital(1)
            display.scroll("Water your plant less!!")
            music.play(music.DADADADUM)
        else:
            display.scroll("The moisture is perfect!")
            led_green.write_digital(1)
            led_red.write_digital(0)
            music.play(music.NYAN)
    else:
        display.scroll("Error!!")
