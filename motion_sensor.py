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
    GPIO.setup(SensorPin, GPIO.IN)
    GPIO.output(BuzzerPin, GPIO.LOW)


def buzz_on():
    # print 'On'
    GPIO.output(BuzzerPin, True)

def buzz_off():
    # print 'Off'
    GPIO.output(BuzzerPin, False)

def destroy():
    GPIO.output(BuzzerPin, False)
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
        print 'Starting...'
        time.sleep(2)
        while True:
            if GPIO.input(23):
                loop(3)
                # beep(0.5)
                print 'Motion Detected!'
                time.sleep(5)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()