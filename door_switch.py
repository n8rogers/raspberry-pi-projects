import RPi.GPIO as GPIO
import time

SENSOR = 4
BUZZER = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR, GPIO.IN)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.output(BUZZER, GPIO.LOW)

def destroy():
    GPIO.cleanup()

def beep(x):
    buzz_on()
    time.sleep(x)
    buzz_off()
    time.sleep(x)

def loop(x):
    while x > 0:
        beep(0.1)
        x = x - 1

if __name__ == '__main__':
    setup()
    try:
        While True:
            if not GPIO.input(SENSOR):
                loop(3)

    except KeyboardInterrupt:
        destroy()