import RPi.GPIO as GPIO
import time

Buzzer = 24
Sensor = 23

def setup():
    global BuzzerPin = Buzzer
    global SensorPin = Sensor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)

def buzz_on():
    GPIO.output(BuzzerPin, GPIO.LOW)

def buzz_off():
    GPIO.output(BuzzerPin, GPIO.HIGH)

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        print 'Starting...'
    except KeyboardInterrupt:
        destroy()