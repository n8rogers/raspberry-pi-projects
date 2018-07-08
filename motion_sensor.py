import RPi.GPIO as GPIO
import time, buzzer

BUZZER = 24
Sensor = 23

def setup():
    global buzz
    global SensorPin
    global Door1Pin
    GPIO.setmode(GPIO.BCM)
    buzz = buzzer.Buzzer(GPIO, BUZZER)
    Door1Pin = Door1
    SensorPin = Sensor
    GPIO.setup(SensorPin, GPIO.IN)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        print 'Starting...'
        time.sleep(2)
        while True:
            if GPIO.input(SensorPin):
                buzz.beep_count(3, 0.1)
                print 'Motion Detected!'
                time.sleep(5)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()