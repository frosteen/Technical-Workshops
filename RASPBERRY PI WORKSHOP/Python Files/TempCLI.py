from w1thermsensor import W1ThermSensor
import time

tempSensor = W1ThermSensor()

while True:
    tempC = tempSensor.get_temperature()  # Celsius
    tempF = tempSensor.get_temperature(W1ThermSensor.DEGREES_F)  # Farenheit
    tempK = tempSensor.get_temperature(W1ThermSensor.KELVIN)  # Kelvin
    print("Temperature: {0} C, {1} F, {2} K".format(tempC, tempF, tempK))
    time.sleep(1)
