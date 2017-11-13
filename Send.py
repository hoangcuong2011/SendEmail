"""
send text string (e.g. status) via Gmail SMTP
"""
import smtplib
from email.mime.text import MIMEText
from getpass import getpass

def sender(user:str, passw:str, to:list, textmsg:str, server:str):
    """
    this is not a good way to do things.
    Should use Oauth.
    """
    with smtplib.SMTP_SSL('smtp.gmail.com') as s:
        s.login(user, passw)

        msg = MIMEText(textmsg)

        msg['Subject']= 'System status update'
        msg['From']= user
        msg['To'] = ', '.join(to)

        s.sendmail(user,to, msg.as_string())
        s.quit()

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('user',help='Gmail username')
    p.add_argument('to',help='email address(es) to send to', nargs='+')
    p.add_argument('-s','--server',help='SMTP server',default='smtp.gmail.com')
    p = p.parse_args()
    
    testmsg="just testing my email from Python setup"

    sender(p.user+'@gmail.com',
           getpass('gmail password: '),
           p.to,
           testmsg, 
           p.server)
