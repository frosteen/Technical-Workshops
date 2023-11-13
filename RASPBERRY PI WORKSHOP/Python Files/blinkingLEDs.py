import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.HIGH)

    while True:
        GPIO.output(7, GPIO.LOW)
        time.sleep(1)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exit mo")
