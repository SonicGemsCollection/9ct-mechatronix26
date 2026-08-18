#welcome to the main.py

"""description of file
 this file is where the code should be. it should be what runs on the pico you should have.
 load this file onto there."""

# this sets up the components.
import machine
import utime

# set up lights
led1 = machine.Pin(15, machine.Pin.OUT)

# this sets up variables.
temp = 0
humidval = 0
humidon = 0
hoton = 0
junk = 0
switch = True
switchon = 1
neenaw = 440
aah = 0


# this is where the main routine (main) should start

# turn power led on to tell you that it's on
def main():
    while switch == True:
        input("this is where the main routine should begin. This does nothing currently, by the way. Wanna test?")
        if temp <= 37:
            # good. go to next part. just to make sure, set a junk value that is there to make sure code doesnt go bad.
            junk = 1
        elif temp > 37:
            # panic!
            hoton = 1
            burn()
        else:
            # somethings wrong
            print("The programmer has a nap.")
            print("Hold out! Programmer!")
            input("Error in temperature checking routine.")
        # humidity checking
        if humidval <= 45:
            # good. loop. No junk value setting this time, except as a placeholder.
            # loop
            junk = 0
        elif humidval > 45:
            # panic!
            humidon = 1
        else:
            # somethings wrong
            print("The programmer has a nap.")
            print("Hold out! Programmer!")
            input("Error in humidity checking routine.")


'''This part here is where i can tell you what a specific routine should do.
This is where the start of the code is gonna be so far. It will maintain basically the entire thing.'''

'''This section is where i can write test code where i dont mess up the entire thing.

start
# temperature checking
if temp =< 37:
    # good. go to next part.
elif temp > 37:
    # panic!
    hoton = 1
# humidity checking
if humidval =< 45:
    # good. loop.
    loop
if humidval > 45:
    # panic!
    humidon = 1

'''
# this is where the main routine (main) should end



# this is where the too hot routine (burn) should start
'''This part here is gonna be when the sensor detects over 37°C.
It will scream at you in double intervals and shine an LED.
If this works first try it is guaranteed one of my Atari 2600 Q*Bert carts will be Q*Bert's Qubes.'''

def burn():
    # if also humid, start a new thing, end self and humid.
    if humidon == 1:
        aah = 1
        humidon = 0
        hoton = 0
        end
    # if not humid, do this.
    elif hoton == 1:
        while hoton == 1:
            # if cool
            if temp <= 37:
                # phew, we're fine now.
                hoton = 0
                end
            #if still hot
            elif temp > 37:
                # we're not good at all
                # beep twice and shine led
                # wait for 2 secs
                # loop
                for i in range:
                    led1.value(1) # shines the led
                    utime.sleep(0.3)  # Wait for 0.3 seconds
                    led1.value(0) # turns off the led
                    utime.sleep(0.3)  # Wait for 0.3 seconds, repeat until okay.
            #if something goes wrong
            else:
                print("The programmer has a nap.")
                print("Hold out! Programmer!")
                input("Error in hot routine.")
# this is where the too hot routine (burn) should end



# this is where the too humid routine (sweat) should start
'''This part here is gonna be when the sensor detects over 45% humidity.
It will scream at you in single intervals and shine an LED.
It is relatively similar to the burn routine, only slightly modified.'''

'''def sweat():
    # if predefined both variable is on, end.
    if aah == 1:
        end
    elif humidon == 1:
        while humidon == 1:
            # if dry
            if humidval <= 45:
                # good
                humidon = 0
                end
            # if still humid
            elif humidval > 45:
                # not good
                # beep once and show different led
                # wait for 2 secs
                # loop. junk value as a placeholder.
                junk = 19
            #if something goes wrong
            else:
                print("The programmer has a nap.")
                print("Hold out! Programmer!")
                input("Error in humid routine.")'''

# this is where the too humid routine (sweat) should end

# this is where the too hot and humid routine (dying) should start
'''This part is gonna be when both sensors exceed their values.
It will scream at you in triple intervals and shine 2 LEDs.
It will be a unique routine.'''

'''def dying():
    while aah == 1:
        # if still in panic
        if humidval > 45 and temp > 37:
            # scream in triple intervals and show both leds
            # wait for 1 sec #this is serious stuff here this is urgent
            # loop
            # temp junk value
            junk = 29
        # if humid is back:
        elif humidval <= 45 and temp > 37:
            # better.
            hoton = 1
            aah = 0
            end
        # if hot is back:
        elif humidval > 45 and temp <= 37:
            #meh
            humidon = 1
            aah = 0
            end
        # in exceptional cases where both hot and humid are back at the same time:
        elif humidval <= 45 and temp <= 37:
            #grest job (great)
            aah = 0
            end
        # if something goes wrong:
        else:
            print("The programmer has a nap.")
            print("Hold out! Programmer!")
            input("Error in humid and hot routine.")'''
# this is where the too hot and humid routine (dying) should end

# this is where the on/off routine (onoff) should begin.
'''def onoff():
    while True:
        if switchon == 1 or switchon == True:
        # do nothing, still on
            switch == True
        elif switchon == 0 or switchon == False:
        # turn off
            switch == False 
        else:
            print("The programmer has a nap.")
            print("Hold out! Programmer!")
            input("Error in on / off routine.")'''''


# this is where the program all begins.
#onoff()
main()