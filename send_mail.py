import smtplib
from email.message import EmailMessage


email = 'python.hank@gmail.com'
password = 'H8523574569512h'
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:

    mail.login(email, password)
    
    # constructing an email messege to be sent
    messege = EmailMessage()
    messege['To'] = 'hassanien.kaissi@gmail.com'  # or a list or emails or a comma seperated string or emails
    messege['From'] = email
    messege['Subject'] = 'Testing smtp mail'
    messege.set_content('This is a test of the smtp python email sending\nwith an attachment')
    
    # adding an attachment
    file = open('automate/pythex.org.PNG', 'rb')
    attachment = file.read()
    messege.add_attachment(attachment, maintype='application', subtype='octet-stream', filename='regex cheatsheet.png')

    # sending HTML email 
    html = '''<!DOCTYPE html><html><body><h1>This is an HTML Heading</h1><p>and its paragraph</p></body></html>'''
    

    # if have a text and attachment and want to add html have to add the alternative to text part
    text_part, attachment_part = messege.iter_parts()
    text_part.add_alternative(html, subtype='html')

    mail.send_message(messege)