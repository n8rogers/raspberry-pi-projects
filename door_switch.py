import RPi.GPIO as GPIO
import time, active_buzzer, switch

SENSOR = 4
BUZZER = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    global buzz
    global switch
    buzz = buzzer.Buzzer(GPIO, BUZZER)
    switch = switch.Switch(GPIO, SENSOR)

def destroy():
    GPIO.cleanup()

def door_open():
    print("Door Open")
    while True:
        if switch.is_high():
            break

def door_closed():
    print("Door Closed")
    while True:
        if switch.is_low():
            break

if __name__ == '__main__':
    setup()
    try:
        while True:
            if switch.is_high():
                buzz.beep_count(1, 0.5)
                door_closed()
            else:
                buzz.beep_count(3, 0.1)
                door_open()
    except:
        destroy()
