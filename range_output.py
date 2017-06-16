import time
from Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
BUTTON = 21
LIGHT = 22

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LIGHT, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

while True:
    if GPIO.input(BUTTON) == True:
        lcd.clear()
        lcd.message("Distance Measured\n" + str(get_distance())


