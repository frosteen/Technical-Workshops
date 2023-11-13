import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

try:

	while True: 
		if(GPIO.input(23) ==1):
			print("Button 1 pressed")
			 
		if(GPIO.input(24) == 0): 
			print("Button 2 pressed")

except KeyboardInterrupt:
	GPIO.cleanup()