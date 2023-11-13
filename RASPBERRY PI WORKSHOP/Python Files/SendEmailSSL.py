import smtplib

user = "luispambid@gmail.com"
pw = "pambid614"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(user, pw)
server.sendmail(user, user, "your message")
server.close()
print("Email sent")
