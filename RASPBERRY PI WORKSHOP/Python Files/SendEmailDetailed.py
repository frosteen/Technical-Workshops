import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = "iecep.raspberry@gmail.com"
pw = "1234567890"

email = MIMEMultipart()
email["From"] = user
email["To"] = user
email["Subject"] = "Email Alert"
body = "Mesage Body"
email.attach(MIMEText(body, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, pw)
server.sendmail(user, user, email.as_string())
server.close()
print("Email sent")
