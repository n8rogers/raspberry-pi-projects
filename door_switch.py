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

if __name__ == '__main__':
    setup()
    try:
        closed = True
        while closed:
            if not GPIO.input(SENSOR):
                buzz.beep_count(3, 0.1)
    except KeyboardInterrupt:
        destroy()
