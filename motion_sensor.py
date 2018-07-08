import RPi.GPIO as GPIO
import time, active_buzzer, switch

BUZZER = 24
SENSOR = 23

def setup():
    global buzz
    global motion
    global SensorPin
    GPIO.setmode(GPIO.BCM)
    buzz = buzzer.Buzzer(GPIO, BUZZER)
    motion = switch.Switch(GPIO, SENSOR)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        print 'Starting...'
        time.sleep(2)
        while True:
            if motion.is_high():
                buzz.beep_count(3, 0.1)
                print 'Motion Detected!'
                time.sleep(5)
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()