import RPi.GPIO as GPIO
import time
 
led = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
												
try:
	while True:
		GPIO.output(led,True)
		time.sleep(0.5)
		GPIO.output(led,False)
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()

