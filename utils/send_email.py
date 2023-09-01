import threading
from django.core.mail import EmailMessage


class SendEmail(threading.Thread):

    def __init__(self, email_object):
        threading.Thread.__init__(self)
        self.email_object = email_object

    def run(self):
        self.email_object.send()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'],
            to=[data['to_email']])
        SendEmail(email).start()
