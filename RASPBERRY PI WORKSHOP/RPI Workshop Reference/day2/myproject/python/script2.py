import webiopi
from webiopi.devices.serial import Serial

GPIO=webiopi.GPIO

# initialize Serial driver
serial = Serial("ttyUSB0", 9600)

LIGHT=18

def setup():

        GPIO.setFunction(LIGHT,GPIO.OUT)
        
        while (serial.available() > 0):
                serial.readString()
        
def loop():

        if (serial.available() > 0):
                data = serial.readString()
                if (data>20):
                        GPIO.digitalWrite(LIGHT, GPIO.HIGH)
	
	webiopi.sleep(1)
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
