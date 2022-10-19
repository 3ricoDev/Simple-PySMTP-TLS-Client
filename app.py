"""
Author: Érico Oliveira
email: 3rico.dev@gmail.com
Date: 19/Out/2022

<< Simple pySMTP Client With TLS Support >>

This simple application was built to test connectivity with external SMTP servers
using a TLS connection (as gmail).

It will interact with the user to get the SENDER, RCPT, SUBJECT and BODY.

Enjoy!

:wq!

"""

# 1 - Imports
# Multipart - Gets all the fields (source, destination, subject...)
from email.mime.multipart import MIMEMultipart
# Text - (Gets the email's body.)
from email.mime.text import MIMEText
# SMTP lib
import smtplib
# GUI
from PySimpleGUI import PySimpleGUI as gui

# 2 - Send Email Function

def send_mail(smtp_server, smtp_port, smtp_user, smtp_passwd, mail_rcpt, mail_subject, mail_body):
    msg = MIMEMultipart()
    msg['from'] = smtp_user
    msg['to'] = mail_rcpt
    msg['subject'] = mail_subject

    body = MIMEText(mail_body) # MIMEText(msg_body, 'html')
    msg.attach(body)
    # 3- Send Email
    with smtplib.SMTP(host=smtp_server, port=smtp_port) as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(smtp_user, smtp_passwd)
            smtp.send_message(msg)
            # print(' Your email was sent successfully! =) ')
            result = ' Your email was sent successfully! =) '
            return result
        except Exception as e:
            # print('Fail to send your email. =( ')
            # print('Error: ', e)
            message = str(e)
            return message


# 3 - Main Window (Get Parameters)


def window1():
    gui.theme('Reddit')
    layout = [
        [gui.Push(), gui.Text('Welcome to the Simple pySMTP-TLS client ! ', font='bold'), gui.Push()],
        [gui.Push(), gui.Text(''), gui.Push()],
        [gui.Text('SMTP Server: ', justification='left', expand_x=True), gui.Input(key='smtp_server', size=(20, 1))],
        [gui.Text('SMTP TLS Port: ', justification='left', expand_x=True), gui.Input(key='smtp_port', size=(20, 1))],
        [gui.Text('Mail User: ', justification='left', expand_x=True), gui.Input(key='smtp_user', size=(20, 1))],
        [gui.Text('Mail Password: ', justification='left', expand_x=True), gui.Input(key='smtp_passwd', size=(20, 1)
            , password_char='*')],
        [gui.Text('Mail Subject: ', justification='left', expand_x=True), gui.Input(key='mail_subject', size=(20, 1))],
        [gui.Text('Mail To: ', justification='left', expand_x=True), gui.Input(key='mail_rcpt', size=(20, 1))],
        [gui.Text('Mail Body: ', justification='left', expand_x=True), gui.Input(key='mail_body', size=(20, 100)
            , expand_x=True, expand_y=True)],
        [gui.Button('SEND')]
    ]
    return gui.Window("<< Simple pySMTP-TLS client >>", layout, finalize=True, size=(380, 400))

# 4 - Second Window (Result)


def window2(smtp_server, smtp_port, smtp_user, smtp_passwd, mail_rcpt, mail_subject, mail_body):
    gui.theme('Reddit')
    layout2 = [
        [gui.Text(str(send_mail(
            smtp_server, smtp_port, smtp_user, smtp_passwd, mail_subject, mail_rcpt, mail_body
        )))]
    ]
    window1.close()
    return gui.Window("<< Simple pySMTP-TLS client >>", layout2, finalize=True)

# 5 - Execute App


window1 = window1()
while True:
    # window, events, values = window1.read()
    window, events, values = gui.read_all_windows()
    if events == gui.WINDOW_CLOSED:
        break
    if events == 'SEND':
        smtp_server = values['smtp_server']
        smtp_port = values['smtp_port']
        smtp_user = values['smtp_user']
        smtp_passwd = values['smtp_passwd']
        mail_subject = values['mail_subject']
        mail_rcpt = values['mail_rcpt']
        mail_body = values['mail_body']
        window2 = window2(smtp_server, smtp_port, smtp_user, smtp_passwd, mail_subject, mail_rcpt, mail_body)