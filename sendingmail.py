import smtplib
from email.message import EmailMessage

def send_email(subject,body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "semionvictor7@gmail.com"
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login("semionvictor7@gmail.com", 'password')
        smtp.send_message(msg)

send_email("Application letter", "please employed me", "codeakstan@gmail.com")