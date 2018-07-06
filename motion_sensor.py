import RPi.GPIO as GPIO
import time

Buzzer = 24
Sensor = 23

def setup():
    global BuzzerPin
    BuzzerPin = Buzzer
    global SensorPin
    SensorPin = Sensor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)

def buzz_on():
    print 'On'
    GPIO.output(BuzzerPin, GPIO.LOW)

def buzz_off():
    print 'Off'
    GPIO.output(BuzzerPin, GPIO.HIGH)

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()

def beep(x):
    buzz_on()
    time.sleep(x)
    buzz_off()
    time.sleep(x)

def loop():
    while True:
        beep(0.5)

if __name__ == '__main__':
    setup()
    try:
        print 'Starting...'
        loop()
    except KeyboardInterrupt:
        destroy()