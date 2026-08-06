#welcome to the main.py

"""description of file
 yadda yadda yadda blah blah blah
 this file is where the code should be. code code code sounds"""

# this sets up variables.
hotvalue = 0
humidval = 0

# this is where the main routine (main) should start
def main():
    while True:
        input("this is where the main routine should begin. This does nothing currently, by the way.")

'''This part here is where i can tell you what a specific routine should do.
This is where the main bulk of the code is gonna be. It will maintain basically the entire thing.'''

'''This section is where i can write test code where i dont mess up the entire thing.

start
# temperature checking
if temp =< 30:
    # good. go to next part.
elif temp > 30:
    # panic!
    hotvalue = 1

'''
# this is where the main routine (main) should end



# this is where the too hot routine (burn) should start
'''This part here is gonna be when the sensor detects over 30°C.
It will scream at you in double intervals and shine an LED.'''

'''def burn():
    # if also humid, start a new thing, end self and humid.
    if humidval == 1:
        aah = 1
        humidval = 0
        hotvalue = 0
        end
    # if not humid, do this.
    elif hotvalue == 1:
        while hotvalue == 1:
        # if cool
        if temp =< 30:
            # phew, we're fine now.
            hotvalue == 0
            end
        #if still hot
        elif temp > 30:
            # we're not good at all
            # beep twice and shine led
            # wait for 2 secs
            # loop'''
# this is where the too hot routine (burn) should end



# this is where the too humid routine (sweat) should start
'''This part here is gonna be when the sensor detects over 45% humidity.
It will scream at you in single intervals and shine an LED.'''

'''def sweat():
if aah == 1:
    end
while humidval == 1:
    # beep once and show different led
    # wait for 2 secs'''
# this is where the too humid routine (sweat) should end

# this is where the too hot and humid routine (dying) should start
'''This part is gonna be when both sensors exceed their values.
It will scream at you in triple intervals and shine 2 LEDs.'''

'''def dying():
while aah == 1:
    # scream in triple intervals and show both leds
    # wait for 1 sec ''''''this is serious stuff here this is urgent''' ''''''
# this is where the too hot and humid routine (dying) should end