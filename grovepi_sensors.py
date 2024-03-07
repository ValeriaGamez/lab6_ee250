import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
    try:
        # Read distance value from Ultrasonic Ranger
        distance = grovepi.ultrasonicRead(ultrasonic_ranger)
        # Read threshold value from potentiometer
        threshold = grovepi.analogRead(potentiometer)

        # Determine whether object is within threshold distance
        if distance < threshold:
            # Print top line with threshold and "OBJ PRES"
            setRGB(255, 0, 0)  # Set text color to red
            setText_norefresh("{:.2f} OBJ PRES".format(threshold))
        else:
            # Print top line with just threshold
            setRGB(0, 255, 0)  # Set text color to green
            setText_norefresh("{:.2f}".format(threshold))

        # Print bottom line with current ultrasonic ranger output
        setRGB(0, 0, 255)  # Set text color to blue
        setCursor(1, 0)  # Move cursor to the beginning of the second line
        setText_norefresh("{:.2f}".format(distance))

        # Wait for a while before updating the LCD again
        time.sleep(0.5)

    except IOError:
        print("Error")