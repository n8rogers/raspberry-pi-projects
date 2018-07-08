import time

class Buzzer:

    def __init__(self, gpio, pin):
        global GPIO
        global PIN
        GPIO = gpio
        PIN = pin
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.LOW)

    def __buzz_on(self):
        GPIO.output(PIN, GPIO.HIGH)

    def __buzz_off(self):
        GPIO.output(PIN, GPIO.LOW)

    def beep(self, x):
        self.__buzz_on()
        time.sleep(x)
        self.__buzz_off()
        time.sleep(x)
    
    def beep_count(self, count, duration):
        while count > 0:
            self.beep(duration)
            count = count - 1
