from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Emiliano Perez"
message["to"] = "exhall.nunez@gmail.com"
message["subject"] = "This is a test"
body = template.substitute(name= "Andres")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("emiliano.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("perezmurilloemi24@gmail.com", "Soyunhit1") 
    smtp.send_message(message)
    print("Sent...")


