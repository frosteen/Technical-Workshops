import smtplib

user = "iecep.raspberry@gmail.com"
pw = "1234567890"

server = smtplib.SMTP("smtp.gmail.com", 587)  # *
server.starttls()  # *
server.login(user, pw)
server.sendmail(user, user, "your message")
server.close()  # *
print("Email sent")
