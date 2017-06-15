#GPIO Testing

import RPi.GPIO as GPIO
import time

light = 22
button = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    if !GPIO.input(button)
        GPIO.output(light,1)

    if GPIO.input(button):
        GPIO.output(light,0)
