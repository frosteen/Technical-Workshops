import RPi.GPIO as GPIO
import time 

pwm = (10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0)

frequency = 60
numSeconds = 1	#Number of Seconds each light strength

refPWM = 0

highTime = 1.0
lowTime = 1.0



def setPWM(pwmPercent):
	global highTime 
	highTime = (1/float(frequency)) * pwmPercent/100

	global lowTime 
	lowTime = (1/float(frequency)) * (100-pwmPercent)/100

def callbackButton1(channel):
	global refPWM
	refPWM = refPWM + 1
	if refPWM >= len(pwm):
		refPWM = 0
	setPWM(pwm[refPWM])


def callbackButton2(channel):
	global refPWM
	refPWM = refPWM - 1
	if refPWM < 0:
		refPWM = len(pwm) - 1
	setPWM(pwm[refPWM])

# Start of program
GPIO.setmode(GPIO.BCM) 


#Setup Input Pins
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

GPIO.add_event_detect(23, GPIO.RISING, callback=callbackButton1, bouncetime=200)
GPIO.add_event_detect(24, GPIO.FALLING, callback=callbackButton2, bouncetime=200)

#Setup Output Pins
GPIO.setup(14,GPIO.OUT)

setPWM(10.0)

try:
	while True:
		GPIO.output(14, True)
		time.sleep(highTime)
		GPIO.output(14, False)
		time.sleep(lowTime)

except KeyboardInterrupt:
	GPIO.cleanup()
