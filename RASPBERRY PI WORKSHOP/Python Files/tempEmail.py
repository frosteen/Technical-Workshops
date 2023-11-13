from tkinter import *
from w1thermsensor import W1ThermSensor
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = "iecep.raspberry@gmail.com"
pw = "rasp0998"

tempSensor = W1ThermSensor()
root = Tk()
w = StringVar()
tempC = 0


def buttonLeft():
    email = MIMEMultipart()
    email["From"] = email_user
    email["To"] = email_user
    email["Subject"] = "Temperature Alert"
    body = "Temperature: {0} Celsius".format(tempC)
    email.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, pw)

    server.sendmail(email_user, email_user, email.as_string())
    server.close()
    print("EmailSent")


def main():
    root.title("Title of your Window")
    root.geometry("300x200")  # width x height
    root.configure(background="white")

    label = Label(root, textvariable=w).pack()
    button = Button(root, text="Button 1", command=buttonLeft).pack(side=LEFT, fill=Y)
    button2 = Button(root, text="Button 2").pack(side=RIGHT, fill=Y)


def readTemperature():
    global tempC
    tempC = tempSensor.get_temperature()
    print(tempC)
    w.set("Temperature: %s Celsius" % tempC)


def read_interval():
    readTemperature()
    root.after(1000, read_interval)


main()
read_interval()
root.mainloop()
