import RPi.GPIO as GPIO
import time, buzzer

SENSOR = 4
BUZZER = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    global buzzer = buzzer.Buzzer(GPIO, BUZZER)
    GPIO.setup(SENSOR, GPIO.IN)

def destroy():
    GPIO.cleanup()



def closed():

if __name__ == '__main__':
    setup()
    try:
        closed = True
        While closed:
            if not GPIO.input(SENSOR):
                buzzer.beep_count(3, 0.1)

    except KeyboardInterrupt:
        destroy()