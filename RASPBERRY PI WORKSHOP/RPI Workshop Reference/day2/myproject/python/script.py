import webiopi

GPIO=webiopi.GPIO

LIGHT=18

def setup():

	GPIO.setFunction(LIGHT,GPIO.OUT)

def loop():
	if (GPIO.digitalRead(LIGHT) == True):
		 GPIO.digitalWrite(LIGHT, GPIO.HIGH)

	if (GPIO.digitalRead(LIGHT) == False):
		GPIO.digitalWrite(LIGHT, GPIO.LOW)
	
	webiopi.sleep(1)
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
