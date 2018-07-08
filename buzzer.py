import time

class Buzzer:

    def __init__(self, GPIO, PIN):
        global gpio
        global pin
        gpio = GPIO
        pin = PIN
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def __buzz_on():
        GPIO.output(pin, GPIO.HIGH)

    def __buzz_off():
        GPIO.output(pin, GPIO.LOW)

    def beep(x):
        __buzz_on()
        time.sleep(x)
        __buzz_off()
        time.sleep(x)
    
    def beep_count(self, count, duration):
        while count > 0:
            beep(duration)
            count = count - 1
