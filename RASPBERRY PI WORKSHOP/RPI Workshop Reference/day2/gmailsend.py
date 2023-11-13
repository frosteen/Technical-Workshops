import smtplib
from email.mime.text import MIMEText

print "Sending email"
USERNAME = "jokeman.santos"
PASSWORD = "petermark"
MAILTO = "pm.delacruz@yahoo.com"

msg= MIMEText('Testing')
msg['Subject'] = 'RPi3 mail Testing'
msg['From'] = USERNAME
msg['To'] = MAILTO

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo_or_helo_if_needed()
server.starttls()
server.ehlo_or_helo_if_needed()
print "logging in"
server.login(USERNAME,PASSWORD)
print "sending mail"
server.sendmail(USERNAME, MAILTO, msg.as_string())
print "quitting"
server.quit()
print "done"

