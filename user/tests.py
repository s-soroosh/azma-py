from django.test import TestCase
from django.core.mail import send_mail


def fake_test():
    send_mail('SUBJECT ', 'Hello man', 'azmaweb@zareie.net', ['soroosh.sarabadani@gmail.com', 'mahdi.elf@gmail.com'],fail_silently=False)
