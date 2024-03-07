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
    setText_norefresh(str(threshold))
    # print(threshold)
    # print(distance)
    
    # TODO: format LCD text according to threshhold
    # setText_norefresh(threshold)

    # if distance < threshold:
    #   setText(threshold, "cm OBJ PRES")
    


    
  
    
  except IOError:
    print("Error")