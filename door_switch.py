import RPi.GPIO as GPIO
import time, buzzer

SENSOR = 4
BUZZER = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    global buzz 
    buzz = buzzer.Buzzer(GPIO, BUZZER)
    GPIO.setup(SENSOR, GPIO.IN)

def destroy():
    GPIO.cleanup()

def door_open():
    print("Door Open")
    while True:
        if GPIO.input(SENSOR):
            break

def door_closed():
    print("Door Closed")
    while True:
        if not GPIO.input(SENSOR):
            break

if __name__ == '__main__':
    setup()
    try:
        while True:
            if GPIO.input(SENSOR):
                door_closed()
            else:
                buzz.beep_count(3, 0.1)
                door_open()
    except:
        destroy()
