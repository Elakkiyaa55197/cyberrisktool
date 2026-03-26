import smtplib

def send_alert():

    sender = "elakkiviswa@gmail.com"
    receiver = "elakkiviswa@gmail.com"
    password = "elakki@!552007"

    subject = "CRITICAL ALERT: Vulnerability detected"

    message = f"""Subject:{subject}

High or Critical vulnerability detected.

Target URL: example.com
Risk Score: 8.5

Recommended Action:
Fix SQL Injection
Fix XSS

This is an automated alert.
"""

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender,password)

    server.sendmail(sender,receiver,message)

    server.quit()

send_alert() 