import RPi.GPIO as GPIO 

def callbackButton1(channel):
	print "Button 1 pressed"
	print channel


def callbackButton2(channel):
	print "Button 2 pressed"
	print channel


# Start of program

GPIO.setmode(GPIO.BCM) 

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) 


GPIO.add_event_detect(23, GPIO.RISING, callback=callbackButton1, bouncetime=200)

GPIO.add_event_detect(24, GPIO.FALLING, callback=callbackButton2, bouncetime=200)

while True:
	n = 1

GPIO.cleanup()





