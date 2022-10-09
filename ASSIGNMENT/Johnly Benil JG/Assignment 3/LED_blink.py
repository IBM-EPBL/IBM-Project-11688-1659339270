import RPi.GPIO as GPIO
from time import sleep 

#initialization or setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

#Blinking loop
while True: 
 GPIO.output(8, GPIO.HIGH) 
 sleep(1) 
 GPIO.output(8, GPIO.LOW)
 sleep(1)