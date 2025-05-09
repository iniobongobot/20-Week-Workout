import asyncio
import time
from uscis_visa_bullentin import *
from send_google_email import send_email
from secrets_vault import  sender_email, sender_password
import logging

def run():
    subject = ''
    recipient = ['Ini', "9842687656@vtext.com", 'cary']
    # recipients = [['Ini', "9842687656@vtext.com", 'cary']]

    try:
        message = final_output()
        send_email(subject, message, sender_email, sender_password, recipient[1])
    except Exception as e:
        print(e)
        logging.error(e)


if __name__ == '__main__':
     run()


