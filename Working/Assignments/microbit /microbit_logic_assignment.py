from microbit import *
import music 

#assign pins 
sound = pin0
moisture_sensor = pin1
led_red = pin2
led_green = pin3 
servo = pin8

tune = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8",
        "E:4", "F", "G:8"]
tune2 = ["D4:4", "E4:4", "F4:4", "D4:4", "E4:4", "F4:4", "D4:4", "E4:4",
        "F4:4", "G4:4", "D4:8", "G4:4", "D4:4", "G4:8"]

while True:
    #sensor temperature 
    if button_a.is_pressed:
        #check if temperature is equal to 30 degrees celecius
         if accelerometer.was_gesture('shake'):
            display.scroll(temperature())
            if temperature.read_digital() ==  30:
                led_green.write_digital(3)
                music.play(music.tune)
                display.scroll("The temperature is perfect!")
            elif temperature.read_digital() > 30:
                display.scroll("Put your plant somewhere cooler!!") 
                led_red.write_digital(2)
                music.play(tune2)
            else:
                display.scroll("Put your plant somewhere hotter!!") 
                led_red(2)
                music.play(tune2)

       
    elif button_b.is_pressed: 
        #check if the moisture level is equal to 50.
        if mositure_sensor.read_digital() == (50): 
            led_green(3)
            music.play(tune)
            display.scroll("The moisture is perfect!")
        elif mositure_sensor.read_digital() > 50:
            display.scroll("Your moisture level is", moisture_sensor.read_digit)
            display.scroll("Water your plant less!!") 
            led_red(2)
            music.play(tune2)
        else: 
            display.scroll("Your moisture level is", moisture_sensor.read_digit)
            display.scroll("Water your plant more!!") 
            led_red(2)
            music.play(tune2)
    else: 
        display.scroll("Error!!")