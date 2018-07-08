class Switch:

    def __init__(self, gpio, pin):
        global GPIO
        global PIN
        GPIO = gpio
        PIN = pin
        GPIO.setup(PIN, GPIO.IN)
    
    def is_high(self):
        return GPIO.input(PIN)

    def is_low(self):
        return not GPIO.input(PIN)