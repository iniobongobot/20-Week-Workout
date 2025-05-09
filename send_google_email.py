import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(subject, body, sender_email, sender_password, recipient_emails):
    # Create a list of recipient email addresses

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))



    # Connect to Yahoo's SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    try:
        server = smtplib.SMTP(smtp_server)
        server.connect(smtp_server, smtp_port)
        # server.set_debuglevel(True)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_emails, msg.as_string())
        logging.info("Email sent successfully")

    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")

    finally:
        server.quit()
