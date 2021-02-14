import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']= 'sathvik balyapelli'
email['to']= 'blithe.lpu@gmail.com'
email['subject']= 'my first mail via python'

email.set_content('this is BSS')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('sathvik.b999@gmail.com','9010095100bss')
        smtp.send_message(email)
        print('all good')
