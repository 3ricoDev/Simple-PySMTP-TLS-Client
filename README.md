# Simple-PySMTP-TLS-Client
Simple SMTP client in Python with TLS support

1 - Uses PySimpleGui to get:
  smtp_server    SMTP Server to use
  smtp_port      TLS Port (usually 587)
  smtp_user      User mail account
  smtp_passwd    User's password
  mail_rcpt      Email destination
  mail_subject   Email subject
  mail_body      Email Content

2 - Uses SMTPLIB and MIME libs to build and send the email

3 - Uses PySimpleGui to print:
  a) Success Message
  OR
  b) SMTP Server's Error message


## TO_DO
> Allign the input boxes close to the text
> Set the 'Mail_Body" input box to use multiple lines


:wq!
