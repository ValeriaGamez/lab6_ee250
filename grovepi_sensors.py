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
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)
    
    # TODO: read threshold from potentiometer
    threshold = grovepi.analogRead(potentiometer)
    
    # TODO: format LCD text according to threshhold
    # setText_norefresh(threshold)

    if distance > threshold:
        setRGB(0, 255, 0)
        setText_norefresh(str(threshold) + "\n" + str(distance))
    else:
       setRGB(255, 0, 0)
       setText_norefresh(str(threshold) + "cm OBJ PRES" + "\n" + str(distance))
       
    
  except IOError:
    print("Error")