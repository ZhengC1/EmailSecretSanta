import emails
import json
from random import choice

def send_email(giftor_name, giftor_email, giftee_name):
    body = f"<p>Hey {giftor_name}!<br> You get {giftee_name}"
    subject = "Your secret santa"
    sender = ('bubby', 'santa@northpole.com')
    smtp_host = {'host': 'aspmx.l.google.com', 'timeout': 5}
    message = emails.html(html=body, subject=subject, mail_from=sender)
    result = message.send(to="zhengc42@gmail.com", smtp=smtp_host)

with open("recipients.json", 'r') as f:
    recipients =json.loads(f.read())

hat = list(recipients)

for name, email in recipients.items(): 
    giftee = choice([a for a in hat if a != name])
    hat.remove(giftee)
    #print(f"hey {name}\n \t you get {giftee}")
    send_email(name, email, giftee) 
