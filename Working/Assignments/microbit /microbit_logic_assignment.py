from microbit import *
import music 

#assign pins 
sound = pin0
moisture_sensor = pin2
led_red = pin3 
led_green = pin4 
servo = pin8

tune = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8",
        "E:4", "F", "G:8"]
tune2 = ["D4:4", "E4:4", "F4:4", "D4:4", "E4:4", "F4:4", "D4:4", "E4:4",
        "F4:4", "G4:4", "D4:8", "G4:4", "D4:4", "G4:8"]

while True:
    #sensor temperature 
    if button_a.is_pressed:
        #check if temperature is equal to 30 degrees celecius
        if microbit.temperature.read_digit ==  30:
            led_green(4)
            music.play(tune)
            display.scroll("The temperature is perfect!")
        elif microbit.temperature.read_digit > 30:
            display.scroll("Your tempeture is", microbit.temperature.read_digit)
            display.scroll("Put your plant somewhere cooler!!") 
            led_red(3)
            music.play(tune2)
        else:
            display.scroll("Your tempeture is", microbit.temperature.read_digit)
            display.scroll("Put your plant somewhere hotter!!") 
            led_red(3)
            music.play(tune2)

       
    elif button_b.is_pressed: 
        #check if the moisture level is equal to 50.
        if mositure_sensor.read_digit() == 50: 
            led_green(4)
            music.play(tune)
            display.scroll("The moisture is perfect!")
        elif mositure_sensor.read_digit() > 50:
            display.scroll("Your moisture level is", moisture_sensor.read_digit)
            display.scroll("Water your plant less!!") 
            led_red(3)
            music.play(tune2)
        else: 
            display.scroll("Your moisture level is", moisture_sensor.read_digit)
            display.scroll("Water your plant more!!") 
            led_red(3)
            music.play(tune2)
    else: 
        display.scroll("Error!!")