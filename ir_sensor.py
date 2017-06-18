import time
import RPi.GPIO as GPIO
import irsend

GPIO.setmode(GPIO.BCM)

BUTTON = 26

GPIO.setup(BUTTON, GPIO.IN)

def send_once():
    irsend.send_once("Vizio","KEY_POWER")

def start_ir():
    irsend.send_start("Vizio","KEY_POWER")

def stop_ir():
    irsend.send_stop("Vizio","KEY_POWER")


try: 
    while True:
        if GPIO.input(BUTTON) == True:
            start_ir()
            time.sleep(2.0)
            stop_ir()

finally:
    print "Cleaning GPIO"
    GPIO.cleanup()

