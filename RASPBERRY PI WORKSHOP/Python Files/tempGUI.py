from tkinter import *
from w1thermsensor import W1ThermSensor

tempSensor = W1ThermSensor()
root = Tk()
w = StringVar()


def main():
    root.title("Title of your Window")
    root.geometry("300x200")  # width x height
    root.configure(background="white")

    label = Label(root, textvariable=w).pack()
    button = Button(root, text="Button 1").pack(side=LEFT, fill=Y)
    button2 = Button(root, text="Button 2").pack(side=RIGHT, fill=Y)


def readTemperature():
    tempC = tempSensor.get_temperature()
    print(tempC)
    w.set("Temperature: %s Celsius" % tempC)


def read_interval():
    readTemperature()
    root.after(1000, read_interval)


main()
read_interval()
root.mainloop()
