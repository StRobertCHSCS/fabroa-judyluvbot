from microbit import *

# Microbit exchange words 
signal = none
while True:
    if button_a.is_pressed():
        pin1.write_digital(1)
        sleep(100)
        pin1.write_digital(0)
 
        signal = pin2.read_digital()
        if signal == 1:
            display.scroll("Hello")
        else: 
            display.scroll("Error")

display.clear()