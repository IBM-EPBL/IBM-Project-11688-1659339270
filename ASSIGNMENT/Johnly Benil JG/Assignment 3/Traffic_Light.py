import RPi.GPIO as GPIO
import time
import signal
import sys

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#loop for the traffic light function
while True: 
    # Red 
    GPIO.output(8, True) 
    time.sleep(3)  
    # Yellow before green
    GPIO.output(8, False) 
    GPIO.output(9, True) 
    time.sleep(1)  
    # Green 
    GPIO.output(8, False) 
    GPIO.output(9, False) 
    GPIO.output(10, True) 
    time.sleep(5)  
    # Yellow
    GPIO.output(10, False) 
    GPIO.output(9, True) 
    time.sleep(2)  
    # Yellow going off before red begins
    GPIO.output(10, False)